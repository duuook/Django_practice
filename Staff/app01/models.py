from django.db import models


# Create your models here.
class Department(models.Model):
    """部门表"""
    title = models.CharField(max_length=32, verbose_name='部门名称')  # 部门名称
    # code = models.BigAutoField(max_length=32, verbose_name='部门编号')  # 部门编号


class UserInfo(models.Model):
    """用户表"""
    name = models.CharField(max_length=32, verbose_name='姓名')  # 姓名
    age = models.IntegerField(verbose_name='年龄')  # 年龄
    password = models.CharField(max_length=32, verbose_name='密码')  # 密码
    salary = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='薪资', default=0)  # 薪资
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # 创建时间

    # 产生外键约束，实现多表联合
    # 1. to='Department'：关联的表
    # 2. to_field="部门编号"：关联的字段
    # 3. on_delete=models.CASCADE：级联删除,删除部门表中的数据时，用户表中的数据也会被删除
    # 4. verbose_name='部门编号'：字段名
    # 在django中，外键字段默认会在字段名后面加_id
    depart = models.ForeignKey(to='Department', to_field="id", on_delete=models.CASCADE,
                               verbose_name='部门编号')  # 部门ID

    # 置空
    # depart = models.ForeignKey(to='Department', to_field="部门编号", on_delete=models.SET_NULL,null=True,blank=True)

    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)  # 性别
