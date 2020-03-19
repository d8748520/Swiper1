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
