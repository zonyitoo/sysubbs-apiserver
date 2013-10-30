import requests

from base import *
from user import login

def get_mailbox_info(cookies):
    r = requests.get(get_mailbox_info_site, cookies=cookies)
    return r.json()

def get_maillist(cookies, start):
    r = requests.get(get_maillist_info_site, cookies=cookies, params={'start': start})
    return r.json()

def get_mail_content(cookies, index):
    r = requests.get(get_mail_content_site, cookies=cookies, params={'index': index})
    return r.json()

def send_mail(cookies, title, content, receiver):
    r = requests.post(send_mail_site, cookies=cookies, data={'title': title, 'content': content, 'receiver': receiver})
    return r.json()

def del_mail(cookies, indexes): # something wrong
    r = requests.post(del_mail_site, cookies=cookies, data={'indexes': indexes})
    return r.text

if __name__ == '__main__':
    login_data = login('okone', '8612001')
    cookie = login_data['cookie']

    get_mailbox_data = get_mailbox_info(cookie)
    print "get_mailbox_info, response: %s" % get_mailbox_data

    get_maillist_data = get_maillist(cookie, 10)
    print "get_maillist_data, response: %s" % get_maillist_data

    get_mail_content_data = get_mail_content(cookie, 2)
    print "get_mail_content_data, response: %s" % get_mail_content_data

    send_mail_data = send_mail(cookie, 'test', 'test jsbbs api', 'zhongyut')
    print "send_mail_data, response: %s" % send_mail_data

    #del_mail_data = del_mail(cookie, (3, ))
    #print "del_mail_data, response: %s" % del_mail_data
