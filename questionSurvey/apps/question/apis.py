# coding: utf-8
from __future__ import unicode_literals

from common.models import *
from common.db_helper import DB
from io import BytesIO
from dateutil.relativedelta import relativedelta
import pandas
from compiler import ast
import json
import datetime
import copy
from common.logger import Logger
from itertools import chain



logger = Logger.getLoggerInstance()


def test_hello():
    data = test.objects.all().values('name', "addr")
    return list(data)