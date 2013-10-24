import requests
import json

from test_basic import server_publickey, HOST, get_request_header

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
    pass

def get_user_avatar():
    pass

def update_user_avatar():
    pass

if __name__ == '__main__':
    print "get_friends: %s" % get_friends()
    print "add_friend: %s" % add_friend()
    print "del_friend: %s" % del_friend()
    print "get_fav_boards: %s" % get_fav_boards()
    print "del_fav_board: %s" % del_fav_board()
    print "add_fav_board: %s" % add_fav_board()
    print "get_user_info: %s" % get_user_info()

