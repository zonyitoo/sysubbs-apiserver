import json
import unittest
import logging
logger = logging.getLogger()

from test_auth import *
from test_basic import get_request_header

from server.app import init_app
app = init_app().test_client()

HOST = "/mail"

def get_mail_box_info(access_token):
    resp = app.get(HOST + "/get_mail_box_info/", headers=get_request_header(access_token))
    return json.loads(resp.data)

def get_mail_list(access_token):
    resp = app.get(HOST + "/get_mail_list/0/", headers=get_request_header(access_token))
    return json.loads(resp.data)

def get_mail_info(access_token):
    resp = app.get(HOST + "/get_mail_info/1/", headers=get_request_header(access_token))
    return json.loads(resp.data)

def send_mail(access_token):
    data = {'title': 'Test Send Mail',
            'content': 'Test Send Mail',
            'receiver': 'zhongyut'
            }
    resp = app.post(HOST + "/send_mail/", headers=get_request_header(access_token), data=json.dumps(data))
    return json.loads(resp.data)

def del_mail(access_token):
    data = {'mails': [1, ]
            }
    resp = app.post(HOST + "/del_mail/", headers=get_request_header(access_token), data=json.dumps(data))
    return json.loads(resp.data)

class TestMail(unittest.TestCase):
    def setUp(self):
        self.server_publickey, self.login_token = get_server_publickey()
        self.access_token, self.expire = get_access_token(self.server_publickey, self.login_token)
        logger.info('login succeed. Got access_token: %s' % self.access_token)

    def test_get_mail_box_info(self):
        resp = get_mail_box_info(self.access_token)
        self.assertTrue(resp['success'])

    def test_get_mail_list(self):
        resp = get_mail_list(self.access_token)
        self.assertTrue(resp['success'])

    def test_get_mail_info(self):
        resp = get_mail_info(self.access_token)
        self.assertTrue(resp['success'])

    def test_send_mail(self):
        resp = send_mail(self.access_token)
        self.assertTrue(resp['success'])

    #def test_del_mail(self):
    #    resp = del_mail(self.access_token)
    #    self.assertTrue(resp['success'])

    def tearDown(self):
        logger.info('Logout %s' % str(logout(self.access_token, self.server_publickey)))
