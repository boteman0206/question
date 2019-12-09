# coding: utf-8

from __future__ import unicode_literals

from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from common.models import *
from datetime import datetime
from . import apis
from django.utils.http import urlquote
import json


def index(request):
    """
    首页进去
    答一道题目： 记录一次， 中途退出不影响之前的答题
    :param request:
    :return:
    """
    # 获取用户的ip
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
    else:
        ip = request.META.get('REMOTE_ADDR')

    id = request.GET.get('id')
    try:
        if id:
            id = int(id) + 1
            questions = Question.objects.filter(id=id).values('id', 'name', "answer", 'pngname')
        else:
            id = 1

            questions = Question.objects.filter(id= id).values('id', 'name', "answer", 'pngname')
    except Exception:
        raise Exception("id异常")

    for i in list(questions):
        answer = i.get("answer")
        if answer:
            list_answer = answer.split(',')
            i.update(answer=list_answer)
    vm = {'questions': list(questions)}
    # 只管访问页面

    Visit(ip=ip, visit_time=datetime.now(), question_id=id).save()
    return render(request, 'devQues/index.html', vm)


def save(request):
    """
    第一次是从首页跳转过来： 通过id获取下一个答案和题目选项
    需要保存访问的页面
    :param request:
    :return:
    """
    id = request.POST.get('id')
    vm = [{"id": id}]
    # 获取用户的ip
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
    else:
        ip = request.META.get('REMOTE_ADDR')
    # 获取ajax的传值
    answer = request.POST.get('value')
    id = request.POST.get('id')
    print('ip = ', ip)
    print('id = ', id)
    # todo 保存访问的页面答案
    if answer and answer not in ["开始测试", "重新玩一次"]:
        AnswerInformation(ip=ip, question_id=id, answer=answer, create_time=datetime.now()).save()
    if answer == "重新玩一次":  # 重新开始
        vm = [{"id": "0"}]
    if id == "11":  # 需要判断返回12还是13 答案中选择了a就返回12 否则返回13
        datas = AnswerInformation.objects.filter(ip=ip).values('answer').order_by('-create_time')[:10]
        print(datas)
        for data in datas:
            if data.get('answer') in ["是", "非纯母乳喂养", "严重"]:
                vm = [{"id": "12"}]
            else:
                vm = [{"id": "11"}]
            break
    print(vm)
    print(request.COOKIES)
    print(request.session.keys())
    print request.session.session_key
    return JsonResponse(data=vm, safe=False)


def question(request):
    return render(request, 'question.html' )

