# coding: utf-8

from __future__ import unicode_literals

from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from . import apis
from django.utils.http import urlquote
import json


def index(request):
    return render(request, 'index.html')


def question(request):
    '''

    :param request:
    :return:
    '''
    data = apis.test_hello()
    print data
    return render(request, "index.html")

