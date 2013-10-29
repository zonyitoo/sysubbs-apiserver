from test_auth import *
from test_basic import get_request_header
import unittest
import logging
import json
logger = logging.getLogger()

import sys
sys.path.append('..')

from server.app import init_app
app = init_app().test_client()

HOST = '/board'

def get_all_boardname(access_token):
    #resp = requests.get(HOST + '/name/all/', headers=get_request_header(access_token))
    resp = app.get(HOST + '/name/all/', headers=get_request_header(access_token))
    return json.loads(resp.data)

def get_all_boards_info():
    #resp = requests.get(HOST + '/info/all/')
    resp = app.get(HOST + '/info/all/')
    return json.loads(resp.data)

def get_board_info(boardname):
    #resp = requests.get(HOST + ('/info/by_board_name/%s/' % boardname))
    resp = app.get(HOST + ('/info/by_board_name/%s/' % boardname))
    return json.loads(resp.data)

def get_all_boards_info_by_section_code(seccode):
    #resp = requests.get(HOST + ('/info/by_section_code/%s/' % seccode))
    resp = app.get(HOST + ('/info/by_section_code/%s/' % seccode))
    return json.loads(resp.data)

def clear_board_unread(access_token, boardname): #resp = requests.post(HOST + '/clear_board_unread/%s/' % boardname, headers=get_request_header(access_token))
    resp = app.post(HOST + '/clear_board_unread/%s/' % boardname, headers=get_request_header(access_token))
    return json.loads(resp.data)

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.server_publickey, self.login_token = get_server_publickey()
        self.access_token, self.expire = get_access_token(self.server_publickey, self.login_token)
        logger.info('login succeed. Got access_token: %s' % self.access_token)

    def test_get_all_boardname(self):
        resp = get_all_boardname(self.access_token)
        logger.debug('get_all_boardname: %s' % resp)
        self.assertTrue(resp['success'])

    def test_get_all_boards_info(self):
        resp = get_all_boards_info()
        logger.debug('get_all_boards_info: %s' % resp)
        self.assertTrue(resp['success'])

    def test_get_board_info(self):
        resp = get_board_info('water')
        logger.debug('get_board_info(water): %s' % resp)
        self.assertTrue(resp['success'])

    def test_get_all_boards_info_by_section_code(self):
        resp = get_all_boards_info_by_section_code('u')
        logger.debug('get_all_boards_info_by_section_code(u): %s' % resp)
        self.assertTrue(resp['success'])

    def test_clear_board_unread(self):
        resp = clear_board_unread(self.access_token, 'SYSU_Info')
        logger.debug('clear_board_unread(SYSU_Info): %s' % resp)
        self.assertTrue(resp['success'])

    def tearDown(self):
        logger.info('Logout %s' % str(logout(self.access_token, self.server_publickey)))

if __name__ == '__main__':
    unittest.main()
