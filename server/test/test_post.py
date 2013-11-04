from test_auth import *
from test_basic import HOST, get_request_header, get_url_by_role, BaseTestCase
from test_basic import get_binary_content
import unittest
import logging
import json
import base64
logger = logging.getLogger()

import sys
sys.path.append('..')

class TestPost(BaseTestCase):
    def test_get_board_topics_list(self):
        ret = self.client.get(
                    "/post/topic/in/%s/%s/" % ('Test', 0)
                )
        logger.debug('get_board_topics_list: %s' % ret.data)
        self.assertTrue(json.loads(ret.data)['success'])
    def test_get_topic_all_reply(self):
        ret = self.client.get(
                        '/post/topic/replyto/%s/%s/' % ('water', 'M.1383267232.A'),
                    )
        self.assertTrue(json.loads(ret.data)['success'])
    def test_get_topic_page_reply(self):
        ret = self.client.get(
                    '/post/topic/replyto/%s/%s/%s/' % ('water', 'M.1383267232.A', 1),
                )
        self.assertTrue(json.loads(ret.data)['success'])
        ret = self.client.get(
                    '/post/topic/replyto/%s/%s/%s/' % ('water', 'M.1383267232.A', 0),
                )
        self.assertTrue(json.loads(ret.data)['success'])
    def get_post_info(self, boardname, filename):
        ret = self.client.get(
                    '/post/info/%s/%s/' % (boardname, filename)
                )
        self.assertTrue(json.loads(ret.data)['success'])

    def del_topic(self, boardname, topic_id):
        data = {
            'boardname': boardname,
            'id': topic_id,
        }
        ret = self.client.post(
                    get_url_by_role('PostHandler', 'DeletePost'),
                    headers=get_request_header(self.access_token),
                    data=json.dumps(data)
                )
        self.assertTrue(json.loads(ret.data)['success'])

    def reply_topic(self, boardname, filename):
        data = {
            'boardname': boardname,
            'id': filename,
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
        self.del_topic(boardname, delid)

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
        self.get_post_info(data['boardname'], topic_id)

        self.reply_topic(data['boardname'], topic_id)

        data['id'] = topic_id
        data['content'] = data['content'] + '\nTesting Update API.'
        # FIXME: Can't send a attachment, ISSUE #10
        #data['attachment'] = base64.encodestring(get_binary_content('okone_avatar.jpg'))

        ret = self.client.post(
                    get_url_by_role('PostHandler', 'UpdatePost'),
                    headers=get_request_header(self.access_token),
                    data=json.dumps(data)
                )

        retdata = json.loads(ret.data)
        self.assertTrue(retdata['success'])

        self.assertEqual(retdata['data']['id'], topic_id)
        self.get_post_info(data['boardname'], topic_id)

        time.sleep(10)

        self.del_topic(data['boardname'], topic_id)
        
if __name__ == '__main__':
    unittest.main()
