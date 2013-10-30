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
        pass

    def get_mail_list(self, offset):
        """
        get mail list from a specific offset
        methods: GET
        response: mail_list_object
        """
        pass

    def get_mail_info(self, mail_id):
        """
        get a specific mail information according
        to the mail's di
        methods: GET
        response: mail_content_object
        """
        pass

    def send_mail(self):
        """
        send mail!
        methods: POST
        Post data format:
            {'title': mail_title,
             'content': mail_content,
             'receiver': receiver_username}
        response: True or err_code
        """
        pass

    def del_mail(self):
        """
        delete a specific mail according to a list
        of mails' ids
        Post data format:
            {'mails':
            [id1, id2, id3, ....]}
        response: True or err_code
        """
        pass
