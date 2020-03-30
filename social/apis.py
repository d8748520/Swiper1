
from django.http import JsonResponse
from libs.http import render_json
from common import stat
from social import logics
def rcmd_users(request):
    """推荐用户"""
    users = logics.rcmd(request.uid)
    print(users)
    result = [user.to_dict() for user in users]
    return render_json(result)

def like(request):
    """喜欢"""
    sid = request.POST.get("sid")
    result = logics.like_someone(request.uid,sid)



def superlike(request):
    """超级喜欢"""
    pass


def dislike(request):
    """不喜欢"""
    pass

