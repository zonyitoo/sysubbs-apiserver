from flask import make_response

from server.basic.util import get_json_post_data, is_process_success, post_data_format_error
from server.basic.handler import Handler
from server.basic.formatter import fill_fail_format, fill_success_format
from server.processor import SessionProcessor
from jbs_handler import jbsHandler
from server.logger import log_server, log_request
from server.basic.auth import *

class SessionHandler(jbsHandler):
    __handler_name__ = 'session'
    __processor__ = SessionProcessor()

    def get_session_list(self):
        """
        get sessions list
        """
        ret = self.__processor__.get_session_list()
        log_request(api_addr='get_session_list', response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))
