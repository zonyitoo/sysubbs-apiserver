import requests
import json
import StringIO

from test_basic import server_publickey, HOST, get_request_header, save_binary_content, get_binary_content

access_token = "4be6548e-3cd8-11e3-aa62-78e4005393d1"

HOST = HOST + "/user"

def get_friends():
    headers = get_request_header(access_token)

    resp = requests.get(HOST + "/get_friends/", headers=headers)
    return resp.text

def add_friend():
    headers = get_request_header(access_token)

    data = dict(username='okone', alias="okone")
    data = json.dumps(data)
    resp = requests.post(HOST + "/add_friend/", headers=headers, data=data)
    return resp.text

def del_friend():
    headers = get_request_header(access_token)

    data = dict(username="okone")
    data = json.dumps(data)
    resp = requests.post(HOST + "/del_friend/", headers=headers, data=data)
    return resp.text

def get_fav_boards():
    headers = get_request_header(access_token)

    resp = requests.get(HOST + "/get_fav_boards/", headers=headers)
    return resp.json()

def add_fav_board():
    headers = get_request_header(access_token)

    data = dict(boardname="water")
    data = json.dumps(data)
    resp = requests.post(HOST + "/add_fav_board/", headers=headers, data=data)
    return resp.text

def del_fav_board():
    headers = get_request_header(access_token)

    data = dict(boardname="water")
    data = json.dumps(data)
    resp = requests.post(HOST + "/del_fav_board/", headers=headers, data=data)
    return resp.text

def get_user_info():
    resp = requests.get(HOST + "/get_user_info/zhongyut/")
    return resp.json()

def update_user_info():
    headers = get_request_header(access_token)

    data = dict(nickname="ragnarok", gender="M", description=None, signature=None)
    data = json.dumps(data)
    resp = requests.post(HOST + "/update_user_info/", headers=headers, data=data)
    return resp.json()

def get_user_avatar():
    resp = requests.get(HOST + "/get_user_avatar/okone/")
    avatar_binary = resp.content
    save_binary_content(avatar_binary, "okone_avatar.jpg")


def update_user_avatar():
    headers = get_request_header(access_token)
    data = get_binary_content('avatar2.jpg')
    resp = requests.post(HOST + "/update_user_avatar/", headers=headers, data=data)
    return resp.json()

if __name__ == '__main__':
    print "get_friends: %s" % get_friends()
    print "add_friend: %s" % add_friend()
    print "del_friend: %s" % del_friend()
    print "get_fav_boards: %s" % get_fav_boards()
    print "del_fav_board: %s" % del_fav_board()
    print "add_fav_board: %s" % add_fav_board()
    print "get_user_info: %s" % get_user_info()
    print "update_user_info: %s" % update_user_info()
    get_user_avatar()
    print "update_user_avatar: %s" % update_user_avatar()

