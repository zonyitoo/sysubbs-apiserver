from server.basic.util import get_json_post_data, is_process_success, post_data_format_error
from server.basic.handler import Handler
from server.basic.formatter import fill_fail_format, fill_success_format
from server.processor.jbs.postprocessor import PostProcessor
from jbs_handler import jbsHandler
from server.logger import log_server, log_request
from server.basic.auth import *
from server.basic.code import *

class PostHandler(jbsHandler):
    __handler_name__ = 'jbspost'
    __processor__ = PostProcessor()

    def get_board_topics_list(self, start, boardname):
        ret = self.__processor__.get_board_topics_list(start, boardname)
        log_request(api_addr='get_board_topics_list', 
                request={'boardname': boardname}, response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def get_topic_all_reply(self, boardname, topicid):
        ret = self.__processor__.get_topic_all_reply(boardname, topicid)
        log_request(api_addr='get_topic_all_reply', 
                request={'boardname': boardname, 'topic_id': topicid}, 
                response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def get_topic_page_reply(self, boardname, topicid, page):
        ret = self.__processor__.get_topic_page_reply(boardname, topicid, page)
        log_request(api_addr='get_topic_all_reply', 
                request=dict(boardname=boardname, topicid=topicid, page=page),
                response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def get_post_info(self, boardname, topicid):
        ret = self.__processor__.get_post_content(boardname, topicid)
        log_request(api_addr='get_post_info', 
                request=dict(boardname=boardname, topicid=topicid),
                response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def reply_topic(self):
        data = get_json_post_data()
        if not data or 'boardname' not in data\
            or 'id' not in data\
            or 'title' not in data\
            or 'content' not in data\
            or 'attachment' not in data:
                return post_data_format_error()

        ret = self.__processor__.reply_topic(**data)
        log_request(api_addr='reply_topic', request=data, response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def new_topic(self):
        data = get_json_post_data()
        if not data or 'boardname' not in data\
            or 'title' not in data\
            or 'content' not in data\
            or 'attachment' not in data:
                return post_data_format_error()

        ret = self.__processor__.new_topic(**data)
        log_request(api_addr='new_topic', request=data, response=ret)

        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def update_post(self):
        data = get_json_post_data()
        if not data or 'boardname' not in data\
            or 'id' not in data\
            or 'title' not in data\
            or 'content' not in data\
            or 'attachment' not in data:
                return post_data_format_error()

        ret = self.__processor__.update_post(**data)
        log_request(api_addr='update_post', request=data, response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def delete_post(self):
        data = get_json_post_data()
        if not data or 'boardname' not in data\
            or 'id' not in data:
                return post_data_format_error()

        ret = self.__processor__.del_post(**data)
        log_request(api_addr='delete_post', request=data, response=ret)

        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))


