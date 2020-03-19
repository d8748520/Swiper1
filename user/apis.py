from django.http import JsonResponse
from django.core.cache import cache
from user import logics
from common import stat
from user.models import User



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


    return JsonResponse({})
def set_profile(request):


    return JsonResponse({})
def upload_avatar(request):


    return JsonResponse({})