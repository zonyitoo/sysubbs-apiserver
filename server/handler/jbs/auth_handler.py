import json
import time

from flask import request, jsonify

from server.basic.handler import Handler
from server.basic.util import get_json_post_data
from server.basic.auth import *
from server.basic.code import *
from server.basic.formatter import fill_fail_format, fill_success_format
from server.processor import UserProcessor
from server.logger import log_server, log_request
from jbs_handler import jbsHandler

class AuthHandler(jbsHandler):
    __handler_name__ = 'auth'
    __url_prefix__ = '/auth'
    __processor__ = UserProcessor()

    def add_all_view_functions(self):
        self.add_view_func(rule="/deliver_server_publickey/", methods=('GET', ), func=self.deliver_server_publickey)
        self.add_view_func(rule="/request_access_token/", methods=('GET', ), func=self.request_access_token)
        self.add_view_func(rule="/logout/", methods=('GET', ), func=self.logout)

    def deliver_server_publickey(self):
        """
        deliver server's public key, and get client's public key
        methods: GET
        url: '/deliver_server_publickey/'
        post data format (in Authorization header):
            {
                "client_publickey": "..."
            }
        the public key is passed in pkcs#1 format
        """
        client_publickey = get_client_publickey_from_authorization()
        if not client_publickey:
            return make_response(fill_fail_format(err_code=request_data_format_error))
        log_request(api_addr="deliver_server_publickey", request={'client_publickey': client_publickey})
        # generate a new login token
        login_token = gen_login_token()
        # store the new login token into redis
        store_login_token(login_token, {'client_publickey': client_publickey})
        # return the new login_token to the client
        response_value = {'login_token': login_token, 'server_publickey': self.app.config['SERVER_PUBLIC_KEY_PKCS1']}
        response = make_response(fill_success_format())
        response.headers['Authorization'] = json.dumps(response_value)
        log_request(api_addr="deliver_server_publickey", response=response_value)
        return response

    def request_access_token(self):
        """
        request access token, and the server login this user
        methods: GET
        url: '/request_access_token/'
        post data format (in Authorization header):
            {
                "username": username,
                "password": password,
                "login_token": "",
                "nounce": "..."
            }
        and encrypt with server's public key
        """
        client_data = decrypt_client_data(request.headers.get('Authorization', None))
        # check the data if valid
        if not client_data:
            return make_response(fill_fail_format(err_code=request_data_format_error))
        client_data = json.loads(client_data)
        if not ('username' in client_data and
                'password' in client_data and
                'login_token' in client_data and
                'nounce' in client_data):
            log_server(api_addr="request_access_token", msg="client data not provide enough info")
            return make_response(fill_fail_format(err_code=request_data_format_error))
        # first check the login_token if still exist now
        login_token = client_data['login_token']
        login_token_value = get_login_token_value(login_token)
        if not login_token_value:
            return fail_login_token_expired()
        login_token_value = json.loads(login_token_value)
        del_login_token(login_token)
        # login user
        username = client_data['username']
        password = client_data['password']
        ret = self.__processor__.login(username, password)
        cookie = None
        if type(ret) is dict:
            cookie = ret.get('cookie')
            log_server(api_addr="request_access_token", msg="user: %s login success" % username)
        else:
            # login fail
            log_server(api_addr="request_access_token", msg="user: %s login fail, err_code: %s" %
                    (username, ret))
            return make_response(fill_fail_format(err_code=ret))

        nounce = client_data['nounce']
        # get the client public key
        client_publickey = login_token_value.get('client_publickey')
        # generate a new access_token
        access_token = gen_access_token()
        # store the new access_token
        expireat = int(time.time()) + 2592000
        store_access_token(access_token, {'client_publickey': client_publickey,
            'username': username, 'nounce': nounce, 'cookie': cookie, 'expire': expireat}, expireat=expireat)
        ret_val = json.dumps(dict(access_token=access_token, expire=expireat))
        log_request(api_addr="request_access_token", response=ret_val, request=client_data)
        # encrypt ret_val with client_publickey
        ret_val = encrypt_data_by_client_publickey(ret_val, client_publickey)
        response = make_response(fill_success_format())
        response.headers['Authorization'] = ret_val
        return response

    @require_auth
    def logout(self):
        """
        logout user
        methods: GET
        url: '/logout/'
        post data format (in Authorization header):
            {
                "access_token": "..."
                "nounce": "nounce"
            }
        and encrypt with server's public key
        """
        access_token, cookie = self.get_logout_info_from_authorization()
        self.__processor__.set_cookie(cookie)
        # get the cookie and access_token
        log_server(api_addr="logout", msg="logout, cookie: %s" % cookie)
        if cookie:
            logout_ret = self.__processor__.logout()
            if logout_ret is True:
                del_access_token(access_token)
                log_server(api_addr="logout", msg="logout success, del access_token: %s" % access_token)
                return make_response(fill_success_format())
            else:
                log_server(api_addr="logout", msg="logout fail, err_code: %s" % err_code)
                return make_response(fill_fail_format(err_code=ret))
        else:
            del_access_token(access_token)
            log_server(api_addr="logout", msg="logout success, del access_token: %s" % access_token)
            return make_response(fill_success_format())

    def get_logout_info_from_authorization(self):
        user_info = decrypt_client_data(request.headers.get('Authorization', None))
        print user_info
        user_info = json.loads(user_info)
        access_token = user_info.get('access_token')
        cookie = get_cookie_from_access_token(access_token)

        return access_token, cookie
