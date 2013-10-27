import json
import StringIO
import logging
logger = logging.getLogger()

from test_basic import get_request_header, save_binary_content, get_binary_content
from test_auth import *

import sys
sys.path.append('..')

from server.app import init_app
app = init_app().test_client()

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

HOST = "/user"

def get_friends(access_token):
    headers = get_request_header(access_token)

    resp = app.get(HOST + "/get_friends/", headers=headers)
    return json.loads(resp.data)

def add_friend(access_token):
    headers = get_request_header(access_token)

    data = dict(username='okone', alias="okone")
    data = json.dumps(data)
    resp = app.post(HOST + "/add_friend/", headers=headers, data=data)
    return json.loads(resp.data)

def del_friend(access_token):
    headers = get_request_header(access_token)

    data = dict(username="okone")
    data = json.dumps(data)
    resp = app.post(HOST + "/del_friend/", headers=headers, data=data)
    return json.loads(resp.data)

def get_fav_boards(access_token):
    headers = get_request_header(access_token)

    resp = app.get(HOST + "/get_fav_boards/", headers=headers)
    return json.loads(resp.data)

def add_fav_board(access_token):
    headers = get_request_header(access_token)

    data = dict(boardname="water")
    data = json.dumps(data)
    resp = app.post(HOST + "/add_fav_board/", headers=headers, data=data)
    return json.loads(resp.data)

def del_fav_board(access_token):
    headers = get_request_header(access_token)

    data = dict(boardname="water")
    data = json.dumps(data)
    resp = app.post(HOST + "/del_fav_board/", headers=headers, data=data)
    return json.loads(resp.data)

def get_user_info():
    resp = app.get(HOST + "/get_user_info/zhongyut/")
    return json.loads(resp.data)

def update_user_info(access_token):
    headers = get_request_header(access_token)

    data = dict(nickname="ragnarok", gender="M", description=None, signature=None)
    data = json.dumps(data)
    resp = app.post(HOST + "/update_user_info/", data=data, headers=headers)
    return json.loads(resp.data)

def get_user_avatar():
    resp = app.get(HOST + "/get_user_avatar/okone/")
    avatar_binary = resp.data
    save_binary_content(avatar_binary, "okone_avatar.jpg")


def update_user_avatar(access_token):
    headers = get_request_header(access_token)
    data = get_binary_content('avatar2.jpg')
    resp = app.post(HOST + "/update_user_avatar/", data=data, headers=headers)
    return json.loads(resp.data)

class TestUser(unittest.TestCase):
    def setUp(self):
        self.server_publickey, self.login_token = get_server_publickey()
        self.access_token, self.expire = get_access_token(self.server_publickey, self.login_token)
        logger.info('login succeed. Got access_token: %s' % self.access_token)

    def test_get_friends(self):
        resp = get_friends(self.access_token)
        self.assertTrue(resp['success'])

    def test_add_friends(self):
        resp = add_friend(self.access_token)
        self.assertTrue(resp['success'])

    def test_del_friend(self):
        resp = del_friend(self.access_token)
        self.assertTrue(resp['success'])

    def test_get_fav_boards(self):
        resp = get_fav_boards(self.access_token)
        self.assertTrue(resp['success'])

    def test_del_fav_board(self):
        resp = del_fav_board(self.access_token)
        self.assertTrue(resp['success'])

    def test_add_fav_board(self):
        resp = add_fav_board(self.access_token)
        self.assertTrue(resp['success'])

    def test_get_user_info(self):
        resp = get_user_info()
        self.assertTrue(resp['success'])

    def test_update_user_info(self):
        resp = update_user_info(self.access_token)
        self.assertTrue(resp['success'])

    def test_get_user_avatar(self):
        get_user_avatar()

    def test_update_user_avatar(self):
        resp = update_user_avatar(self.access_token)
        self.assertTrue(resp['success'])

    def tearDown(self):
        logger.info('Logout %s' % str(logout(self.access_token, self.server_publickey)))

if __name__ == '__main__':
    '''
    server_publickey, login_token = get_server_publickey()
    access_token, expire = get_access_token(server_publickey, login_token)

    print 'Got access_token %s' % access_token
    print 

    print "get_friends: %s" % get_friends(access_token)
    print "add_friend: %s" % add_friend(access_token)
    print "del_friend: %s" % del_friend(access_token)
    print "get_fav_boards: %s" % get_fav_boards(access_token)
    print "del_fav_board: %s" % del_fav_board(access_token)
    print "add_fav_board: %s" % add_fav_board(access_token)
    print "get_user_info: %s" % get_user_info()
    print "update_user_info: %s" % update_user_info(access_token)
    get_user_avatar()
    print "update_user_avatar: %s" % update_user_avatar(access_token)

    print 'Logout %s' % str(logout(access_token, server_publickey))
    '''

    unittest.main()
