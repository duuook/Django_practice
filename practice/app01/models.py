from django.db import models

# Create your models here.
class UserInfo(models.Model):
    """
    用户信息表
    """
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()