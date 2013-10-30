import requests

from server.basic import BasicMailProcessor
from jbsprocess import jbsProcessorMixin
from urls import *
from server.basic.formatter import fill_fail_format, fill_success_format
from mailformatter import MailBoxFormatter, MailListFormatter, MailContentFormatter

class MailProcessor(BasicMailProcessor, jbsProcessorMixin):
    def get_mailbox_info(self):
        """
        get the mailbox's information, for example,
        the number of mails, total size, used size

        Returns:
            mail_box_object
        """
        # get the total mail number
        r = requests.get(get_mailbox_info_site, cookies=cookies)
        resp = r.json()
        if resp['success']:
            data = resp['data']
            formatter = MailBoxFormatter(data)
            return formatter.format()
        else:
            code = resp['code']
            return code

    def get_mail_list(self, offset):
        """
        get the mail list

        Args:
            offset (int): the start offset, default

        Returns:
            mail_list_object
        """
        r = requests.get(get_maillist_info_site, cookies=cookies, params={'start': offset})
        resp = r.json()
        if resp['success']:
            data = resp['data']
            formatter = MailListFormatter(data)
            return formatter.format()
        else:
            return resp['code']

    def get_mail_info(self, mail_id):
        """
        get the specific mail's information

        Args:
            mail_id (id): the mail's id

        Returns:
            mail_content_object
        """
        r = requests.get(get_mail_content_site, cookies=cookies, params={'index': mail_id})
        resp = r.json()
        if resp['success']:
            data = resp['data']
            formatter = MailContentFormatter(data)
            return formatter.format()
        else:
            return resp['code']

    def send_mail(self, title, content, receiver):
        """
        send mail! =w=

        Args:
            title (str): mail's title
            content (str): mail's content
            receiver (str): mail's receiver

        Returns:
            True, if send success,
            or err_code if fail
        """
        r = requests.post(send_mail_site, cookies=cookies, data={'title': title, 'content': content, 'receiver': receiver})
        resp = r.json()
        if resp['success']:
            return True
        else:
            return resp['code']

    def del_mail(self, id_list):
        """
        delete a mail :(

        Args:
            id_list (list): a list of mails' ids that you want to delete

        Returns:
            True, if delete success, or
            err_code if delete fail
        """
        r = requests.post(del_mail_site, cookies=cookies, data={'indexes': id_list})
        resp = r.json()
        if resp['success']:
            return True
        else:
            return False
