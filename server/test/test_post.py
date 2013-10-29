from test_auth import *
from test_basic import HOST, get_request_header, get_url_by_role, BaseTestCase
import unittest
import logging
import json
logger = logging.getLogger()

import sys
sys.path.append('..')

class TestPost(BaseTestCase):
    def test_get_board_topics_list(self):
        ret = self.client.get(
                    "/post/topic/in/%s/%s/" % ('water', 0)
                )
        logger.debug('get_board_topics_list: %s' % ret)
        self.assertTrue(json.loads(ret.data)['success'])
    def test_get_topic_all_reply(self):
        ret = self.client.get(
                        '/post/topic/replyto/%s/%s/' % ('water', 'M.1382971850.A'),
                    )
        self.assertTrue(json.loads(ret.data)['success'])
    def test_get_topic_page_reply(self):
        ret = self.client.get(
                    '/post/topic/replyto/%s/%s/%s/' % ('water', 'M.1382971850.A', 1),
                )
        self.assertTrue(json.loads(ret.data)['success'])
        ret = self.client.get(
                    '/post/topic/replyto/%s/%s/%s/' % ('water', 'M.1382971850.A', 0),
                )
        self.assertTrue(json.loads(ret.data)['success'])
    def test_get_post_info(self):
        ret = self.client.get(
                    '/post/info/%s/%s/' % ('water', 'M.1382971850.A')
                )
        self.assertTrue(json.loads(ret.data)['success'])

    def del_topic(self, topic_id):
        data = {
            'boardname': 'water',
            'id': topic_id,
        }
        ret = self.client.post(
                    get_url_by_role('PostHandler', 'DeletePost'),
                    headers=get_request_header(self.access_token),
                    data=json.dumps(data)
                )
        self.assertTrue(json.loads(ret.data)['success'])

    def test_reply_topic(self):
        data = {
            'boardname': 'water',
            'id': 'M.1382971850.A',
            'title': 'TestReply',
            'content': "Testing Reply API, Don't Panic",
            'attachment': None
        }
        ret = self.client.post(
                    get_url_by_role('PostHandler', 'ReplyTopic'),
                    headers=get_request_header(self.access_token),
                    data=json.dumps(data)
                )
        self.assertTrue(json.loads(ret.data)['success'])

        delid = json.loads(ret.data)['data']['id']
        import time
        time.sleep(10)
        self.del_topic(delid)

    def test_POST_topic(self):
        data = {
            'boardname': 'water',
            'title': 'TestNewPost',
            'content': "From API Server Team. Testing New Post. Don't Panic.",
            'attachment': None
        }
        ret = self.client.post(
                    get_url_by_role('PostHandler', 'NewTopic'),
                    headers=get_request_header(self.access_token),
                    data=json.dumps(data)
                )

        retdata = json.loads(ret.data)
        self.assertTrue(retdata['success'])

        import time
        topic_id = retdata['data']['id']
        time.sleep(10)

        data['id'] = topic_id
        data['content'] = data['content'] + '\nTesting Update API.'

        ret = self.client.post(
                    get_url_by_role('PostHandler', 'UpdatePost'),
                    headers=get_request_header(self.access_token),
                    data=json.dumps(data)
                )

        retdata = json.loads(ret.data)
        self.assertTrue(retdata['success'])

        self.assertEqual(retdata['data']['id'], topic_id)

        time.sleep(10)

        self.del_topic(topic_id)
        
if __name__ == '__main__':
    unittest.main()
