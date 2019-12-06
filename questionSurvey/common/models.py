# coding: utf8
# __author__ = ""
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class test(models.Model):
    name = models.CharField(max_length=100, help_text="名字")
    addr = models.CharField(max_length=100, help_text="地址")

    class Meta:
        db_table = "test"