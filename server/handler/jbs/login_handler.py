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

class LoginHandler(Handler):
    def __init__(self, *args, **kwargs):
        super(LoginHandler, self).__init__(*args, **kwargs)
        self.user_processor = UserProcessor(self.app)

    def add_all_view_functions(self):
        self.add_view_func(rule="/deliver_server_publickey/", methods=('GET', ), func=self.deliver_server_publickey)
        self.add_view_func(rule="/request_access_token/", methods=('GET'), func=self.request_access_token)

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
        client_publickey = get_client_publickey_from_header()
        if not client_publickey:
            return make_response(fill_fail_format(err_code=request_data_format_error))
        # generate a new login token
        login_token = gen_login_token()
        # store the new login token into redis
        store_login_token(login_token, {'client_publickey': client_publickey})
        # return the new login_token to the client
        response_value = {'login_token': login_token, 'server_publickey': self.app.config['SERVER_PUBLIC_KEY_STR']}
        response = make_response(fill_success_format())
        response.headers['Authorization'] = json.dumps(response_value)
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
        client_data = decrypt_client_data(request.authentication)
        # check the data if valid
        if not client_data:
            return make_response(fill_fail_format(err_code=request_data_format_error))
        if not ('username' in client_data and
                'password' in client_data and
                'login_token' in client_data and
                'nounce' in client_data):
            return make_response(fill_fail_format(err_code=request_data_format_error))
        # first check the login_token if still exist now
        login_token_value = get_login_token_value(login_token)
        if not login_token_value:
            return fail_login_token_expired()
        # login user
        ret = self.user_processor.login(username, password)
        cookie = None
        if type(ret) is dict:
            cookie = ret.get('cookie')
        else:
            # login fail
            return make_response(fill_fail_format(err_code=ret))

        # get the client public key
        client_publickey = login_token_value.get('client_publickey')
        # generate a new access_token
        access_token = gen_access_token()
        # store the new access_token
        store_access_token(access_token, {'client_publickey': client_publickey,
            'username': username, 'nounce': nounce, 'cookie': cookie})
        ret_val = json.dumps(dict(access_token=access_token, expire=int(time.time() + 2592000)))
        # encrypt ret_val with client_publickey
        ret_val = encrypt_data_by_client_publickey(ret_val, client_publickey)
        response = make_response(fill_success_format())
        response.headers['Authorization'] = ret_val
        return response
