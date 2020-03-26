import os
from django.http import JsonResponse
from django.core.cache import cache
from user import logics
from common import stat
from user.models import User
from user.models import Profile
from user.form import ProfileForm
from user.form import UserForm
from libs.qncloud import upload_to_qn


# Create your views here.
def get_vcode(request):
    """用户获取验证码"""
    phonenum = request.GET.get("phonenum")
    success = logics.send_sms(phonenum)
    if success:
        return JsonResponse({"code":stat.OK,"data":None})
    else:
        return JsonResponse({"code":stat.SMS_ERR,"data":None})



def submit_vcode(request):
    """检查验证码，同事进行登录或者注册"""
    vcode = request.POST.get("vcode")
    phonenum = request.POST.get("phonenum")

    key = "Vcode-%s" % phonenum
    print(key)
    cached_vcode = cache.get(key)
    print(cached_vcode)
    if vcode and vcode == cached_vcode:
          #登录  或者  注册
        try:
           user = User.objects.get(phonenum=phonenum)                      #filter  取出来的书questset 获取用户

        except User.DoesNotExist:
           user = User.objects.create(phonenum=phonenum,nickname=phonenum) #创建新用户
        request.session["uid"] = user.id
        return JsonResponse({"code":stat.OK,"data":user.to_dict()})

    else:
        return JsonResponse({"code":stat.VCODE_ERR ,"data":None})



def get_profile(request):
    """获取用户配置"""
    profile, _  =  Profile.objects.get_or_create(id=request.uid)
    return JsonResponse({"code":stat.OK,"data":profile.to_dict()})



def set_profile(request):
    """修改用户信息，及用户配置"""
    user_form = UserForm(request.POST)
    profile_from  = ProfileForm(request.POST)
    #验证 user 表单的数据
    if not user_form.is_valid():
        return JsonResponse({"code":stat.USER_FORM_ERR,"data":user_form.errors})
    #验证 profile 表单的数据
    if not profile_from.is_valid():
        return JsonResponse({"code":stat.PROFILE_FORM_ERR,"data":ProfileForm.errors})
    #修改用户数据
    User.objects.filter(id=request.uid).update(**user_form.changed_data)
    # 修改Profile数据
    Profile.objects.updata_or_create(id=request.uid,defaults=profile_from.changed_data)
    return JsonResponse({"code":stat.OK,"data":None})
        


def upload_avatar(request):
    """上传个人形象"""
    #1.接收用户图片，保存到服务器本地
    avatar_file = request.FILES.get("avatar")
    # print(avatar_file)
    # print("------------------")
    filepath,filename = logics.save_tmp_file(avatar_file)

    print(filename)
    print(filepath)



    #2.上传到七牛云
    url = upload_to_qn(filepath,filename)
    #3.更新用户 avatar 字段
    User.objects.filter(id=request.uid).update(avatar=url)



    #4.删除本地文件
    os.remove(filepath)
    return JsonResponse({"code":stat.OK,"data":None})


    return JsonResponse({})