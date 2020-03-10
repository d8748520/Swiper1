from django.db import models

# Create your models here.
class User(models.Model):
    """user表的数据模型"""
    phonenum = models.CharField(max_length=16,verbose_name="手手机号")
    nickname = models.CharField(max_length=32,verbose_name="昵称")
    gender = models.CharField(max_length=10,verbose_name="性别")
    birthday = models.DateField(default="1900-01-01",verbose_name="出生生年年")
    avatar = models.CharField(max_length=256,verbose_name="个人人形象")
    location = models.CharField(max_length=20,verbose_name="常居地")


