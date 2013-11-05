import json
import requests

from user import login
from base import *

def get_board_posts(start, boardname):
    r = requests.get(get_board_topics_site, params={'type': 'topic', 'start': start, 'boardname': boardname})
    print r.text
    return r.json()

def get_post_content(boardname, filename):
    r = requests.get(get_post_content_site, params={'boardname': boardname, 'filename': filename})
    print r.text
    return r.json()

def get_near_post(boardname, direction, filename):
    r = requests.get(get_near_post_site, params={'boardname': boardname, 'direction': direction, 'filename': filename})
    return r.json()

def get_same_topic_posts(boardname, filename):
    r = requests.get(get_same_topic_posts_site, params={'boardname': boardname, 'filename': filename})
    print r.text
    return r.json()

def add_post(cookies, boardname, post_type, filename, title, content, attach):
    if filename:
        r = requests.post(add_post_site, cookies=cookies, data={'type': post_type, 'boardname': boardname, 'articleid': filename,
            'title': title, 'content': content})
    else:
        r = requests.post(add_post_site, cookies=cookies, data={'type': post_type, 'boardname': boardname,
            'title': title, 'content': content})
    return r.json()

def del_post(cookies, boardname, filename):
    r = requests.post(del_post_site, cookies=cookies, data={'boardname': boardname, 'filename': filename})
    return r.json()

if __name__ == '__main__':
    login_data = login('okone', '8612001')
    cookie = login_data['cookie']

    get_board_posts_data = get_board_posts(0, 'water')
   #print "get_board_posts, response: %s" % get_board_posts_data
    print

    get_post_content_data = get_post_content('water', 'M.1382569831.A')
   #print "get_post_content, response: %s" % get_post_content_data
    print

    get_near_post_data = get_near_post('water', 'prev', 'M.1380338285.A')
    print "get_near_post_data, response: %s" % get_near_post_data

    get_same_topic_posts_data = get_same_topic_posts('water', 'M.1380338285.A')
    print "get_same_topic_posts, response: %s" % get_same_topic_posts_data

    #add_post_data = add_post(cookie, 'water', 'reply', 'M.1379573532.A', 'Re: 2', 'test', None)
    #print "add_post, response: %s" % add_post_data

    #import time
    #time.sleep(10)

    #add_post_data = add_post(cookie, 'water', 'update', add_post_data['data'], 'Re: 2', 'test modified', None)
    #print "add_post, response: %s" % add_post_data

    #del_post_data = del_post(cookie, 'water', add_post_data['data'])
    #print "del_post, response: %s" % del_post_data

    #time.sleep(10)

    #add_post_data = add_post(cookie, 'water', 'new', None, 'Re: 2', 'test', None)
    #print "add_post, response: %s" % add_post_data

    #del_post_data = del_post(cookie, 'water', add_post_data['data'])
    #print "add_post, response: %s" % add_post_data
