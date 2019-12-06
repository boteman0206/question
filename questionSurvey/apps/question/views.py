# coding: utf-8

from __future__ import unicode_literals

from django.http.response import JsonResponse, HttpResponse
from . import apis
from django.utils.http import urlquote
import json


def report_config_list(request):
    '''
    报告->活动有效性评估->报告配置列表
    :param request:
    :return:
    '''
    data = apis.test_hello()
    return JsonResponse(data=data, safe=False)
