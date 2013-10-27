from test_auth import *
from test_basic import HOST, get_request_header
import requests

HOST = HOST + '/board'

def get_all_boardname(access_token):
    resp = requests.get(HOST + '/name/all/', headers=get_request_header(access_token))
    return resp.text

def get_all_boards_info():
    resp = requests.get(HOST + '/info/all/')
    return resp.text

def get_board_info(boardname):
    resp = requests.get(HOST + ('/info/by_board_name/%s/' % boardname))
    return resp.text

def get_all_boards_info_by_section_code(seccode):
    resp = requests.get(HOST + ('/info/by_section_code/%s/' % seccode))
    return resp.text

def clear_board_unread(access_token, boardname):
    resp = requests.post(HOST + '/clear_board_unread/%s/' % boardname, headers=get_request_header(access_token))
    return resp.text

if __name__ == '__main__':
    server_publickey, login_token = get_server_publickey()
    access_token, expire = get_access_token(server_publickey, login_token)

    print 'Got access_token %s' % access_token

    print 'get_all_boardname:'
    print get_all_boardname(access_token)
    print
    
    print 'get_all_boards_info:'
    print get_all_boards_info()
    print

    print 'get_board_info(water):'
    print get_board_info('water')
    print 

    print 'get_all_boards_info_by_section_code(u):'
    print get_all_boards_info_by_section_code('u')
    print

    print 'clear_board_unread(SYSU_Info):'
    print clear_board_unread(access_token, 'SYSU_Info')
    print

    print 'Logout %s' % str(logout(access_token, server_publickey))
