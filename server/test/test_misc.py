import unittest
import logging
import json

logger = logging.getLogger()

from test_auth import *
from test_basic import HOST, get_request_header, get_url_by_role, BaseTestCase

class TestMisc(BaseTestCase):
    def test_get_my_topics(self):
        ret = self.client.get('/misc/get_my_topics/',
                    headers=get_request_header(self.access_token))
        logger.debug('get_my_topics, ret=%s' % ret.data)
        self.assertTrue(json.loads(ret.data)['success'])

    def test_get_newest_topics(self):
        ret = self.client.get('/misc/get_newest_topics/0/')
        logger.debug('get_newest_topics, ret=%s' % ret.data)
        self.assertTrue(json.loads(ret.data)['success'])

