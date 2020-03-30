from django.db import models

# Create your models here.
class Swiped(models.Model):
    """滑动记录"""
    STYPES = (
        ("like","右滑"),
        ("superlike","上滑"),
        ("dislike","左滑")
    )
    uid = models.IntegerField(verbose_name="用户ID")
    sid = models.IntegerField(verbose_name="被滑动的ID")
    stype = models.CharField(max_length=10,choices=STYPES,verbose_name="滑动的类型")
    stime = models.DateTimeField(auto_now_add=True,verbose_name="滑动的时间")
    class Meta:
        unique_together = ("uid","sid")

class Friend(models.Model):
    """好友表"""
    uid1 = models.IntegerField(verbose_name="用户ID")
    uid2 = models.IntegerField(verbose_name="用户ID")

    class Meta:
        unique_together = ("uid1","uid2")



