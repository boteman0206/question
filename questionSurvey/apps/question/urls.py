# coding: utf-8
# __author__: ""
from __future__ import unicode_literals

from django.conf.urls import url, patterns
import views

urlpatterns = patterns("apps.question.views",
    url(r"^hello/$", views.report_config_list),
)
