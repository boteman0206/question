# coding: utf-8
# __author__: ""
from __future__ import unicode_literals

from django.conf.urls import *

urlpatterns = (
    url(r"^question/", include("apps.question.urls")),
)

