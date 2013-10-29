import json
import unittest
import logging
logger = logging.getLogger()

from test_auth import *

from server.app import init_app
app = init_app().test_client()

def get_session_list():
    resp = app.get("/session/get_session_list/")
    return json.loads(resp.data)

class TestSession(unittest.TestCase):
    def setUp(self):
        self.server_publickey, self.login_token = get_server_publickey()
        self.access_token, self.expire = get_access_token(self.server_publickey, self.login_token)
        logger.info('login succeed. Got access_token: %s' % self.access_token)

    def test_get_session(self):
        resp = get_session_list()
        self.assertTrue(resp['success'])

    def tearDown(self):
        logger.info('Logout %s' % str(logout(self.access_token, self.server_publickey)))

if __name__ == '__main__':
    unittest.main()
