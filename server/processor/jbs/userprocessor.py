import requests
import StringIO

from requests.utils import cookiejar_from_dict

from server.basic import BasicUserProcessor
from server.basic.code import no_login
from server.basic.formatter import fill_fail_format, fill_success_format
from urls import *
from userformatter import CookieFormater, FriendsListFormatter, UserFavBoardListFormatter, UserInfoFormatter
from jbsprocess import jbsProcessorMixin


class UserProcessor(BasicUserProcessor, jbsProcessorMixin):
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

    def logout(self):
        """
        logout user
        Returns:
            True, if logout success or
            the error code if logout fail
        """
        #cookie = cookiejar_from_dict({'PHPSESSID': cookie_val})
        r = requests.post(logout_site, cookies=self.cookie)
        resp = r.json()
        if resp['success']:
            return True
        else:
            code = resp['code']
            return code

    def get_friends(self):
        """
        get friends list

        Returns:
            the friends list (dict)
            or the error code if fail
        """
        r = requests.get(get_friends_site, cookies=self.cookie)
        resp = r.json()
        if resp['success']:
            data = resp['data']
            formater = FriendsListFormatter(data)
            return formater.format()
        else:
            return resp['code']

    def add_friend(self, username, alias):
        """
        add a new friend

        Args:
            username (str): the new username
            alias (str): the alias of your new friend
        Returns:
            True, if add success
            err_code, if add fail
        """
        r = requests.post(add_friend_site, data={'id': username, 'exp': alias}, cookies=self.cookie)
        resp = r.json()
        if resp['success']:
            return True
        else:
            return resp['code']

    def del_friend(self, username):
        """
        delete a friend

        Args:
            username (str): your friend's name

        Returns:
            True, if delete success,
            err_code, if delete fail
        """
        r = requests.post(del_friend_site, data={'userid': username}, cookies=self.cookie)
        resp = r.json()
        if resp['success']:
            return True
        else:
            return resp['code']

    def get_fav_boards(self):
        """
        get user fav boards

        Returns:
            the board list object:
            {"boards": ['board object', ...]}
        """
        r = requests.get(get_fav_boards_site, cookies=self.cookie)
        resp = r.json()
        if resp['success']:
            data = resp['data']
            formatter = UserFavBoardListFormatter(data)
            return formatter.format()
        else:
            return resp['code']

    def add_fav_board(self, boardname):
        """
        add a new favorite board

        Args:
            boardname (str): the board name

        Returns:
            True, if add success or
            err_code if fail
        """
        r = requests.post(add_fav_board_site, cookies=self.cookie, data={'boardname': boardname})
        resp = r.json()
        if resp['success']:
            return True
        else:
            return resp['code']

    def del_fav_board(self, boardname):
        """
        delete a favorite board

        Args:
            boardname (str): the boardname

        Returns:
            True, if delete success or
            err_code if fail
        """
        r = requests.post(del_fav_board_site, cookies=self.cookie, data={'boardname': boardname})
        resp = r.json()
        if resp['success']:
            return True
        else:
            return resp['code']

    def get_user_info(self, username):
        """
        get the user info for specfic username

        Args:
            username (str): username

        Returns:
            the user info object
        """
        r = requests.get(query_other_user_site, params={'userid': username})
        resp = r.json()
        if resp['success']:
            data = resp['data']
            formatter = UserInfoFormatter(data)
            return formatter.format()
        else:
            return resp['code']

    def update_user_info(self, nickname=None, gender=None, description=None, signature=None):
        """
        update user info (not include avatar)

        Args:
            nickname (str): the new nickname
            gender (str): the new gender (M or F)
            description (str): the new description
            signature (str): the new signature

        Returns:
            True, if update success or
            err_code if update fail
        """
        data = dict()
        if nickname:
            data['username'] = nickname
        if gender:
            data['gender'] = gender
        if description:
            data['plan'] = description
        if signature:
            data['signature'] = signature
        r = requests.post(update_user_info_site, cookies=self.cookie, data=data)
        resp = r.json()
        if resp['success']:
            return True
        else:
            return resp['code']

    def update_user_avatar(self, avatar_binary):
        """
        update user's avatar

        Args:
            avatar_binary (str): the avatar_binary str

        Returns:
            True, if update success or
            err_code if update fail
        """
        avatar_file = StringIO.StringIO(binary_content)
        files = {'avatar': avatar_file}
        r = requests.post(cookies=self.cookie, url=update_user_info_site, files=files)
        resp = r.json()
        if resp['success']:
            return True
        else:
            return resp['code']

    def get_user_avatar(self, username):
        """
        get user's avatar

        Args:
            username (str): the username

        Returns:
            the avatar binary content
        """
        r = requests.get(url=get_user_avatar_site % username)
        return r.content
