from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Users(AbstractUser):
    """用户"""
    GENDER = (
        ('male', '男'),
        ('female', '女')
    )
    name = models.CharField(verbose_name='姓名', max_length=20, null=True, blank=True)
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    mobile = models.CharField(verbose_name='手机', max_length=11, null=True, blank=True)
    gender = models.CharField(verbose_name='性别', max_length=10, choices=GENDER, default='男')
    email = models.CharField(verbose_name='邮箱', max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class VerifyCode(models.Model):
    """短信验证码，后期保存进redis中"""
    code = models.CharField(max_length=20, verbose_name='手机验证码')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.utcnow)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name
