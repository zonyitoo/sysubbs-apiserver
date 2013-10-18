import requests

from requests.utils import cookiejar_from_dict

from server.basic import BasicUserProcessor
from server.basic.formatter import fill_fail_format, fill_success_format
from urls import *
from userformatter import CookieFormater

class UserProcessor(BasicUserProcessor):
    """
    UserProcessor for jsbbs API
    """

    def register(self):
        """
        NOT open register in this version
        """
        raise NotImplementedError()

    def login(self, username, password):
        """
        login user
        Args:
            username (str): the userid
            password (str): the password

        Returns:
            the login token, that is the cookie, with this format:
            {'PHPSESSID': cookie_value}
            and return in this format:
            {'cookie': cookie_value}
        """
        r = requests.post(login_site, data={"userid": username, "passwd": password})
        resp = r.json()
        if resp['success']:
            cookie = r.cookies.get('PHPSESSID')
            cookie_formatter = CookieFormater(cookie)
            return cookie_formatter.format()
        else:
            code = resp['code']
            return code

    def logout(self, cookie_val):
        """
        logout user
        Args:
            cookie_val (str): the cookie value, will reassembly as 'PHPSESSID:cookie_val'
        Returns:
            True, if logout success or
            the error code if logout fail
        """
        cookie = cookiejar_from_dict({'PHPSESSID': cookie_val})
        r = requests.post(logout_site, cookies=cookie)
        resp = r.json()
        if resp['success']:
            return True
        else:
            code = resp['code']
            return code

    def get_friends(self):
        pass

    def add_friend(self):
        pass

    def del_friend(self):
        pass

    def get_fav_boards(self):
        pass

    def add_fav_board(self):
        pass

    def del_fav_board(self):
        pass

    def get_user_info(self):
        pass

    def update_user_info(self):
        pass

    def get_user_avatar(self):
        pass
