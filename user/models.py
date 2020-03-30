from django.db import models

# Create your models here.
class User(models.Model):
    """user表的数据模型"""
    GENDERS = (
        ("male","男性"),
        ("female","女性")
    )
    LOCATION = (
        ("北京", "北京"),
        ("上海", "上海"),
        ("南京", "南京"),
        ("苏州", "苏州"),
        ("深圳", "深圳"),
        ("无锡", "无锡"),
        ("香港", "香港"),
        ("台湾", "台湾"),
        ("合肥", "合肥"),
    )
    phonenum = models.CharField(max_length=16, unique=True,verbose_name="手手机号")
    nickname = models.CharField(max_length=32,verbose_name="昵称")
    gender = models.CharField(max_length=10,choices=GENDERS,verbose_name="性别")
    birthday = models.DateField(default="1900-01-01",verbose_name="生日")
    avatar = models.CharField(max_length=256,verbose_name="个人人形象")
    location = models.CharField(max_length=20,choices=LOCATION,verbose_name="常居地")

    def to_dict(self):
        return {
        "id":self.id,
        "phonenum":self.phonenum,
        "nickname":self.nickname,
        "gender":self.gender,
        "birthday":str(self.birthday),
        "avatar":self.avatar,
        "location":self.location,

        }

class Profile(models.Model):
    """个人的配置及交友资料"""
    dating_gender = models.CharField(max_length=10,choices=User.GENDERS,verbose_name="性别")
    dating_location =  models.CharField(max_length=20,choices=User.LOCATION,verbose_name="目标城市",)
    min_distance =  models.IntegerField(default=1,verbose_name="最小查找范围",)
    max_distance =  models.IntegerField(default=2,verbose_name="最大查找范围",)
    min_dating_age =  models.IntegerField(default=18,verbose_name="最小交友年年龄",)
    max_dating_age =  models.IntegerField(default=50,verbose_name="最大交友年年龄",)
    vibration =  models.BooleanField(default=True,verbose_name="是否开启震动",)
    only_matche =  models.BooleanField(default=True,verbose_name="不不让为匹配的人人看我的相册",)
    auto_play =  models.BooleanField(default=True,verbose_name="自自动播放视频",)

    def to_dict(self):
        return {
            "id":self.id,
            "dating_gender":self.dating_gender,
            "location":self.location,
            "min_distance":self.min_distance,
            "max_distance":self.max_distance,
            "min_dating_age":self.min_dating_age,
            "max_dating_age":self.max_dating_age,
            "vibration":self.vibration,
            "only_matche":self.only_matche,
            "auto_play":self.auto_play,


        }

