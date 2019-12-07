# coding: utf8
# __author__ = ""
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=100, help_text="名字")
    addr = models.CharField(max_length=100, help_text="地址")

    class Meta:
        db_table = "test"


class Question(models.Model):

    page = models.CharField(max_length=1024, help_text="页面的类型")
    choose = models.CharField(max_length=1024, help_text="测试选项,逗号隔开")
    tips = models.CharField(max_length=1024, help_text="小贴士", null=True, default=None)

    class Meta:
        db_table = "question"


class Visit(models.Model):

    ip = models.CharField(max_length=20, help_text="访问的ip地址")
    visit_time = models.DateTimeField(help_text="访问时间", auto_now_add=True)
    page = models.ForeignKey(Question, help_text="访问题目页面类型")

    class Meta:
        db_table = "visit"


class AnswerInformation(models.Model):

    question = models.ForeignKey(Question, help_text="访问题目页面类型")
    ip = models.CharField(max_length=30, help_text="访问的ip地址")
    answer = models.CharField(max_length=30, help_text="选择的答案")
    create_time = models.DateTimeField(help_text="开始时间", auto_now_add=True)
    end_time = models.DateTimeField(help_text="结束时间", null=True)

    class Meta:
        db_table = "information"
