import json
import requests
import StringIO

from base import *

def register(userid, password, *args, **kwargs):
    """
    not allow
    """
    username = kwargs.get('username')
    realname = kwargs.get('realname')
    address = kwargs.get('address')
    email = kwargs.get('gender')
    birthyear = kwargs.get('birthyear')
    birthmonth = kwargs.get('birthmonth')
    birthday = kwargs.get('birthday')

    data = {"userid": userid, "passwd": password, "passwd-confirm": password}
    if username:
        data['username'] = username
    if realname:
        data['realname'] = realname
    if address:
        data['address'] = address
    if email:
        data['email'] = email
    if gender:
        data['gender'] = gender
    if birthyear:
        data['birthyear'] = birthyear
    if birthmonth:
        data['birthmonth'] = birthmonth
    if birthday:
        data['birthday'] = birthday

    r = requests.post(register_site, data=data)
    return r.json()

def login(username, password):
    r = requests.post(login_site, data={"userid": username, "passwd": password})
    return {"cookie": r.cookies, "data": r.json()}

def logout(cookies):
    r = requests.post(logout_site, cookies=cookies)
    return r.json()

def get_friends(cookies):
    r = requests.get(get_friends_site, cookies=cookies)
    return r.json()

def add_friend(cookie, userid, comment):
    r = requests.post(add_friend_site, data={'id': userid, 'exp': comment}, cookies=cookie)
    return r.json()

def del_friend(cookie, userid):
    r = requests.post(del_friend_site, data={'userid': userid}, cookies=cookie)
    return r.json()

def get_fav_boards(cookies):
    r = requests.get(get_fav_boards_site, cookies=cookies)
    return r.json()

def add_fav_board(cookies, boardname):
    r = requests.post(add_fav_board_site, cookies=cookies, data={'boardname': boardname})
    return r.json()

def del_fav_board(cookies, boardname):
    r = requests.post(del_fav_board_site, cookies=cookies, data={'boardname': boardname})
    return r.json()

def query_other_user(userid):
    r = requests.get(query_other_user_site, params={'userid': userid})
    return r.json()

def query_user_self_info(cookies):
    r = requests.get(get_user_self_info_site, cookies=cookies)
    return r.json()

def update_user_info(cookies, *args, **kwargs):
    passwd = kwargs.get('password')
    old_passwd = kwargs.get('old_passwd')
    username = kwargs.get('username')
    realname = kwargs.get('realname')
    gender = kwargs.get('gender') # M or F
    address = kwargs.get('address')
    email = kwargs.get('email')
    birthyear = kwargs.get('birthyear')
    birthmonth = kwargs.get('birthmonth')
    birthday = kwargs.get('birthday')
    plan = kwargs.get('plan')
    signature = kwargs.get('signature')

    data = {}
    if passwd:
        data['passwd'] = passwd
        data['old-passwd'] = old_passwd
        data['confirm-passwd'] = passwd
    if username:
        data['username'] = username
    if realname:
        data['realname'] = realname
    if gender:
        data['gender'] = gender
    if address:
        data['address'] = address
    if email:
        data['email'] = email
    if birthyear:
        data['birthyear'] = birthyear
    if birthmonth:
        data['birthmonth'] = birthmonth
    if birthday:
        data['birthday'] = birthday
    if plan:
        data['plan'] = plan
    if signature:
        data['signature'] = signature

    print "pudate_user_info, data: %s" % data

    r = requests.post(update_user_info_site, cookies=cookies, data=data)
    return r.json()

def update_user_avatar(cookies, avatar_file):
    files = {'avatar': avatar_file}
    r = requests.post(cookies=cookies, url=update_user_info_site, files=files)
    return r.json()

def get_user_avatar(userid):
    r = requests.get(url=get_user_avatar_site % userid)
    return r.content

def save_binary_content(binary_content, out_filename):
    file_io = StringIO.StringIO(binary_content)
    new_file = open(out_filename, 'w')
    new_file.write(file_io.getvalue())
    new_file.close()
    file_io.close()


if __name__ == '__main__':
    login_data = login('okone', '8612001')
    cookie = login_data['cookie']
    print 'login, \n cookie: %s, \n response: %s ' % (login_data['cookie'], login_data['data'])

    #logout_data = logout(cookie)
    #print 'logout, response: %s' % logout_data

    #get_friends_data = get_friends(cookie)
    #print "get_friends, response: %s" % get_friends_data

    #del_friend_data = del_friend(cookie, 'zhongyut')
    #print "del_friend, response: %s" % del_friend_data

    #add_friend_data = add_friend(cookie, 'zhongyut', 'mimi')
    #print "add_friend, reponse: %s " % add_friend_data

    #get_fav_boards_data = get_fav_boards(cookie)
    #print "get_fav_boards, response: %s" % get_fav_boards_data

    #del_fav_board_data = del_fav_board(cookie, 'Lecture')
    #print "del_fav_board, response: %s" % del_fav_board_data

    #add_fav_board_data = add_fav_board(cookie, 'Lecture')
    #print "add_fav_board, response: %s" % add_fav_board_data

    #query_other_user_data = query_other_user('zhongyut')
    #print "query_other_user, response: %s" % query_other_user_data

    #query_user_self_data = query_user_self_info(cookie)
    #print "query_user_self, response: %s" % query_user_self_data

    update_user_info_data = update_user_info(cookie,
            plan="2B or not 2B? \n mail: okone1288@gmail.com", birthyear=1992, signature='2b or not 2b')
    print "update_user_info, response: %s" % update_user_info_data

    ##update_user_avatar_data = update_user_avatar(cookie, open("avatar1.jpg"))
    ##print "update_user_avatar, reponse: %s" % update_user_avatar_data

    #avatar_binary = get_user_avatar('zhongyut')
    #save_binary_content(avatar_binary, 'testfile.jpg')
