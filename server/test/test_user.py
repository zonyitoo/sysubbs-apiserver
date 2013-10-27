import requests
import json
import StringIO

from test_basic import HOST, get_request_header, save_binary_content, get_binary_content
from test_auth import *

HOST = HOST + "/user"

def get_friends(access_token):
    headers = get_request_header(access_token)

    resp = requests.get(HOST + "/get_friends/", headers=headers)
    return resp.text

def add_friend(access_token):
    headers = get_request_header(access_token)

    data = dict(username='okone', alias="okone")
    data = json.dumps(data)
    resp = requests.post(HOST + "/add_friend/", headers=headers, data=data)
    return resp.text

def del_friend(access_token):
    headers = get_request_header(access_token)

    data = dict(username="okone")
    data = json.dumps(data)
    resp = requests.post(HOST + "/del_friend/", headers=headers, data=data)
    return resp.text

def get_fav_boards(access_token):
    headers = get_request_header(access_token)

    resp = requests.get(HOST + "/get_fav_boards/", headers=headers)
    return resp.json()

def add_fav_board(access_token):
    headers = get_request_header(access_token)

    data = dict(boardname="water")
    data = json.dumps(data)
    resp = requests.post(HOST + "/add_fav_board/", headers=headers, data=data)
    return resp.text

def del_fav_board(access_token):
    headers = get_request_header(access_token)

    data = dict(boardname="water")
    data = json.dumps(data)
    resp = requests.post(HOST + "/del_fav_board/", headers=headers, data=data)
    return resp.text

def get_user_info():
    resp = requests.get(HOST + "/get_user_info/zhongyut/")
    return resp.json()

def update_user_info(access_token):
    headers = get_request_header(access_token)

    data = dict(nickname="ragnarok", gender="M", description=None, signature=None)
    data = json.dumps(data)
    resp = requests.post(HOST + "/update_user_info/", data=data, headers=headers)
    return resp.json()

def get_user_avatar():
    resp = requests.get(HOST + "/get_user_avatar/okone/")
    avatar_binary = resp.content
    save_binary_content(avatar_binary, "okone_avatar.jpg")


def update_user_avatar(access_token):
    headers = get_request_header(access_token)
    data = get_binary_content('avatar2.jpg')
    resp = requests.post(HOST + "/update_user_avatar/", data=data, headers=headers)
    return resp.json()

if __name__ == '__main__':
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
