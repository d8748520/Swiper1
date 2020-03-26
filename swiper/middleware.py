
"""
1.HTTP Server 接收浏览器的发送的“报文”
2.WSGI 将请求报文封装成 httprequest 对象
---------------------------------------------------- process_request
3.Django 进行URL匹配, 找到对应的view 函数
------------------------------------------------------process_view
4.view 函数进行处理：
   1.获取参数
   2.调用数据库、缓存
   3.调用其他程序逻辑
---------------------process_template
   4.进行模板的渲染
   5.将运算结果封装成一个 HTTPresponse对象
------------------------------------------------------process_exception
--------------------------------------------------------process_httpresponse
5.WSGI 将HTTPresponse对象封装成 “响应报文”
6.HTTP server 将响应报文发送给浏览器
7.HTTP server   关闭 浏览器 网络链接

关于 WSGI :
HTTP Sevrer(socket 服务器 ，控制网络链接 接收发送数据）

WSGI

web application


"""
from django.utils.deprecation import  MiddlewareMixin
from django.http import JsonResponse
from common import stat

class AuthMiddleware(MiddlewareMixin):
    """登录检查中间件"""

    white_list = (
                  '/api/user/get_vcode',
                  '/api/user/submit_vcode',
)
    def process_request(self,request):
        #检查当前请求的路径是否在 白名单 中
        if request.path in self.white_list:
            return
        uid = request.session.get("uid")
        print(uid)
        if not uid:
            return JsonResponse({"code":stat.LOGIN_REQUIRED,"data":None})
        else:
            request.uid = uid

