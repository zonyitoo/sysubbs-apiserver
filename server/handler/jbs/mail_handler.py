from flask import make_response

from server.basic.util import get_json_post_data, is_process_success, post_data_format_error
from server.basic.formatter import fill_fail_format, fill_success_format
from server.processor import MailProcessor
from jbs_handler import jbsHandler
from server.logger import log_server, log_request
from server.basic.auth import *

class MailHandler(jbsHandler):
    __handler_name__ = 'mail'
    __processor__ = MailProcessor()

    def get_mail_box_info(self):
        """
        get mail box info
        methods: GET
        response: mail_box_object
        """
        ret = self.__processor__.get_mailbox_info()
        log_request(api_addr='get_mail_box_info', response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(ret))

    def get_mail_list(self, offset):
        """
        get mail list from a specific offset
        methods: GET
        response: mail_list_object
        """
        ret = self.__processor__.get_mail_list(offset)
        log_request(api_addr='get_mail_list', request="offset: %s" % offset, response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(ret))

    def get_mail_info(self, mail_id):
        """
        get a specific mail information according
        to the mail's di
        methods: GET
        response: mail_content_object
        """
        log_request(api_addr='get_mail_info', request="mail_id: %s" % mail_id)
        ret = self.__processor__.get_mail_info(mail_id)
        log_request(api_addr='get_mail_info', request="mail_id: %s" % mail_id, response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(ret))

    def send_mail(self):
        """
        send mail =w=
        methods: POST
        Post data format:
            {'title': mail_title,
             'content': mail_content,
             'receiver': receiver_username}
        response: True or err_code
        """
        data = get_json_post_data()
        log_request(api_addr='send_mail', request=data)
        if not data or (
                'title' not in data or \
                'content' not in data or \
                'receiver' not in data):
            return post_data_format_error()
        ret = self.__processor__.send_mail(**data)
        log_request(api_addr='send_mail', response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format())
        else:
            return make_response(fill_fail_format(ret))

    def del_mail(self):
        """
        delete a specific mail according to a list
        of mails' ids
        Post data format:
            {'mails':
            [id1, id2, id3, ....]}
        response: True or err_code
        """
        data = get_json_post_data()
        log_request(api_addr='del_mail', request=data)
        ret = self.__processor__.del_mail(data['mails'])
        if is_process_success(ret):
            return make_response(fill_success_format())
        else:
            return make_response(fill_fail_format())
