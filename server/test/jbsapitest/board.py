import requests

from user import login
from base import *

def get_all_boardnames(cookies):
    r = requests.get(url=get_all_boardnames_site, cookies=cookies)
    return r.json()

def get_all_boards_info():
    r = requests.get(url=get_all_boards_info_site)
    return r.json()

def get_board_info(boardname):
    r = requests.get(url=get_board_info_site, params={'boardname': boardname})
    return r.json()

def get_boards_info_by_seccode(seccode):
    r = requests.get(get_sec_info_site, params={'sec_code': seccode})
    return r.json()

def clear_board_unread(cookies, boardname):
    r = requests.post(clear_unread_site, data={'boardname': boardname}, cookies=cookies)
    return r.json()


if __name__ == '__main__':
    login_data = login('okone', '8612001')
    cookie = login_data['cookie']

    #boardname_data = get_all_boardnames(cookie)
    #print "get_all_boardnames, response: %s" % boardname_data

    #boards_info_data = get_all_boards_info()
    #print len(boards_info_data['data']['all'])
    #print "get_all_boards_info, response: %s" % boards_info_data['data']['all']

    board_info_data = get_board_info('water')
    print "get_board_info, response: %s" % board_info_data

    boards_info_data = get_boards_info_by_seccode('u')
    print "get_boards_info_by_seccode, response: %s" % boards_info_data

    clear_unread_data = clear_board_unread(cookie, 'SYSU_Info')
    print "clear_board_unread, response: %s" % clear_unread_data


