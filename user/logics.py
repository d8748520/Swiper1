import os
from uuid import uuid4
import random
import requests
from django.core.cache import cache
from swiper import conf
from libs.qncloud import upload_to_qn
from user.models import User
from tasks import celery_app

def gen_rand_code(length=6):
    """产生指定长度的随机码"""
    a=[str(random.randint(0,9)) for i in range(length)]
    return "".join(a)


def send_sms(mobile):
    """发送短信验证码"""
    #检查短信发送状态，防止短时间内给用户重复发送
    key = "Vcode-%s" % mobile
    print(key)
    if cache.get(key):
        return True                  #之前发送过验证码，直接返回True
    vcode =  gen_rand_code()         #产生验证码
    print("验证码：%s" %vcode)
    args = conf.YZX_SMS_ARGS.copy()  #原型模式
    args["param"] = vcode
    args["mobile"] = mobile


    response=requests.post(conf.YZX_SMS_API,json=args)              #访问云之讯的接口   参数必须是json
    if response.status_code == 200:
        result = response.json()
        print(result.get("msg"))
        if result.get("code") == "000000":
            cache.set(key,vcode,360)                              #缓存
            return True
        else:
            return False
    return False

def save_tmp_file(tmp_file):
    tmp_filename = uuid4().hex
    tmp_filepath = "/tmp/%s" % tmp_filename
    with open(tmp_filepath,"wb") as fp:
        for chunk in tmp_file.chunks():
            fp.write(chunk)

    return tmp_filepath,tmp_filename

@celery_app.task
def save_avatar(uid,avatar_file):
    """保存用户形象"""
    filepath, filename = save_tmp_file(avatar_file)
    # 2.上传到七牛云
    url = upload_to_qn(filepath, filename)
    # 3.更新用户 avatar 字段
    User.objects.filter(id=uid).update(avatar=url)
    # 4.删除本地文件
    os.remove(filepath)
