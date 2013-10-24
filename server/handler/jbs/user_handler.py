from flask import make_response

from server.basic.util import get_json_post_data, is_process_success, post_data_format_error
from server.basic.handler import Handler
from server.basic.formatter import fill_success_format, fill_fail_format
from server.processor import UserProcessor
from jbs_handler import jbsHandler
from server.logger import log_server, log_request
from server.basic.auth import *
from server.basic.code import *

class UserHandler(jbsHandler):
    __handler_name__ = 'user'
    __processor__ = UserProcessor()

    @require_auth
    def get_friends(self):
        """
        get user's friend
        """
        ret = self.__processor__.get_friends()
        log_request(api_addr='get_friends', response=friend_ret)
        if is_process_success(ret):
            return make_response(fill_success_format(friend_ret))
        else:
            return make_response(fill_fail_format(err_code=friend_ret))

    @require_auth
    def add_friend(self):
        """
        add a new friend
        post data format:
            {"username": username, "alias": alias}
        """
        data = get_json_post_data()
        if not data or ("username" not in data or "alias" not in data):
            return post_data_format_error()
        ret = self.__processor__.add_friend(**data)
        if is_process_success(ret):
            return make_response(fill_success_format())
        else:
            return make_response(fill_fail_format(err_code=ret))

    @require_auth
    def del_friend(self):
        """
        delete a friend
        post data format:
            {"username": username}
        """
        data = get_json_post_data()
        if not data or "username" not in data:
            return post_data_format_error()
        ret = self.__processor__.del_friend(**data)
        if is_process_success(ret):
            return make_response(fill_success_format())
        else:
            return make_response(fill_fail_format(err_code=ret))

    @require_auth
    def get_fav_boards(self):
        """
        get the fav boards
        """
        ret = self.__processor__.get_fav_boards()
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    @require_auth
    def add_fav_board(self):
        """
        add a new favorite board
        post data format:
            {"boardname": boardname}
        """
        data = get_json_post_data()
        if not data or "boardname" not in data:
            return post_data_format_error()
        ret = self.__processor__.add_fav_board(**data)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    @require_auth
    def del_fav_board(self):
        """
        delete a favorite board
        post data format:
            {"boardname": boardname}
        """
        data = get_json_post_data()
        if not data and "boardname" not in data:
            return post_data_format_error()
        ret = self.__processor__.del_fav_board(**data)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def get_user_info(self, username):
        """
        get user's info for 'username'
        """
        ret = self.__processor__.get_user_info(username)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    @require_auth
    def update_user_info(self):
        """
        update user's info, except avatar
        post data format:
            {"nickname": nickname, "gender": M or F,
             "description": description, "signature": signature}
        if you don't update some part of userinfo, just pass null
        for this key
        """
        data = get_json_post_data()
        if not data or \
            ("nickname" not in data
                    or "gender" not in data
                    or "description" not in data
                    or "signature" not in data):
            return post_data_format_error()
        ret = self.__processor__.update_user_info(**data)
        if is_process_success(ret):
            return make_response(fill_success_format())
        else:
            return make_response(fill_fail_format(err_code=ret))

    @require_auth
    def update_user_avatar(self):
        """
        update user avatar
        post data:
            the new avatar binary data
        """
        data = request.data
        ret = self.__processor__.update_user_avatar(data)
        if is_process_success(ret):
            return make_response(fill_success_format())
        else:
            return make_response(fill_fail_format(err_code=ret))

    def get_user_avatar(self, username):
        """
        get user avatar
        """
        ret = self.__processor__.get_user_avatar(username)
        if ret:
            return make_response(ret)
        else:
            return make_response(fill_fail_format(err_code=get_user_avatar_fail))
