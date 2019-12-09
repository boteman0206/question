from __future__ import unicode_literals

from django.http.response import JsonResponse
from common.logger import Logger
from common.exception import NeedCodeException
from common.exception import LockedException

from website.settings import *
import traceback

logger = Logger.getLoggerInstance()

HTTP_200_OK = 200
HTTP_400_BADREQUEST = 400
HTTP_401_UNAUTHORIZED = 401
HTTP_402_LOCKED = 402
HTTP_403_FORBIDDEN = 403
HTTP_412_NEEDCODE = 412
HTTP_413_SESSION_TIMEOUT = 413
HTTP_414_ALREADY_LOGIN = 414

class MpMiddleware:
    # _build_response_with_code
    def _build_response_with_code(self, msg, code):
        response = JsonResponse(dict(msg=msg), safe=False)
        response.status_code = code
        return response

# GatewayMiddleware
class GatewayMiddleware(MpMiddleware):
    def process_request(self, request):
        if request.path.startswith('/static/'):
            return

    def process_exception(self, request, exception):
        logger.error(traceback.format_exc().decode('utf-8'))

        if isinstance(exception, NeedCodeException):
            return self._build_response_with_code(unicode(exception), HTTP_412_NEEDCODE)

        elif isinstance(exception, LockedException):
            return self._build_response_with_code(unicode(exception), HTTP_402_LOCKED)
        else:
            return self._build_response_with_code(unicode(exception), HTTP_400_BADREQUEST)