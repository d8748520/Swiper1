import datetime
from user.models import User
from user.models import Profile
def rcmd(uid):
    """用户推荐接口"""
    #获取当前用户的交友资料
    profile, _ = Profile.objects.get_or_create(id=uid)
    #计算出生日期
    today = datetime.date.today()
    earliest_biarthday = today - datetime.timedelta(profile.max_dating_age*365)#最早出生日期
    latest_biarthday = today - datetime.timedelta(profile.min_dating_age*365)  #z最晚出生日期
    #根据条件匹配要推荐的用户
    users = User.objects.filter(gender=profile.dating_gender,
                        location=profile.dating_location,
                        birthday__gte=earliest_biarthday,
                        birthday__lte=latest_biarthday)[:20]

    #TODO:过滤出已经划过的用户

    #返回最终结果
    return users


def like_someone(uid,sid):
    """右滑"""
    #添加一条滑动记录（不允许重复滑动某人）


    #检查是否可以匹配成好友

