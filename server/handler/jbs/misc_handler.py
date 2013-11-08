from flask import make_response

from server.basic.util import get_json_post_data, is_process_success
from server.basic.handler import Handler
from server.basic.formatter import fill_fail_format, fill_success_format
from server.basic.code import unknown_error
from jbs_handler import jbsHandler
from server.logger import log_server, log_request
from server.processor import MiscProcessor

class MiscHandler(jbsHandler):
    __handler_name__ = 'misc'
    __processor__ = MiscProcessor()

    def get_my_topics(self):
        """
        get my topics
        """
        ret = self.__processor__.get_my_topic()
        log_request(api_addr='get_my_topics', response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=unknown_error))

    def get_newest_topics(self, offset):
        """
        get newest topics
        """
        log_server(api_addr='get_newest_topics', msg='in get newest topics, offset=%s' % offset)
        ret = self.__processor__.get_new_topic(offset)
        log_request(api_addr='get_newest_topics', response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=unknown_error))
