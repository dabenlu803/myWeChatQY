from __future__ import unicode_literals

from django.db import models


class DepartmentInfo(models.Model):
    id = models.AutoField(primary_key=True)
    department_id = models.IntegerField(unique=True)
    department_name = models.CharField(max_length=50)
    parent_id = models.IntegerField()
    order = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=20, unique=True)
    user_name = models.CharField(max_length=50)
    department_id = models.CommaSeparatedIntegerField(max_length=50)
    position = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    gender = models.IntegerField()
    email = models.EmailField()
    weixin_id = models.CharField(max_length=20)
    avatar = models.URLField()
    status = models.IntegerField()
    extr_attr = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)












