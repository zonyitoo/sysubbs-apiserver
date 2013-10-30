from server.basic.processor import BasicPostProcessor
from jbsprocess import jbsProcessorMixin
import requests
from urls import *
from postformatter import *
import StringIO
from server.logger import log_server, log_request

class PostProcessor(BasicPostProcessor, jbsProcessorMixin):
    """
    BasicPostProcessor, used to get/set posts' information
    """
    def get_board_topics_list(self, start, boardname):
        """
        get a specific board's topic list
        """
        r = requests.get(get_board_topics_site, params={'type': 'topic', 'start': start, 'boardname': boardname})
        resp = r.json()
        if resp['success']:
            formatter = TopicListFormatter(resp['data'])
            return formatter.format()
        else:
            return resp['code']

    def get_topic_all_reply(self, boardname, topicid):
        """
        get a specific topic's all replies
        """
        # Get all replies filename
        r = requests.get(get_same_topic_posts_site, params={'boardname': boardname, 'filename': topicid})
        resp = r.json()
        if not resp['success']:
            return resp['code']
        
        # Get content details
        replys = []
        for filename in resp['data']:
            r = requests.get(get_post_content_site, params={'boardname': boardname, 'filename': filename})
            try:
                resp = r.json()
            except ValueError:
                continue
            if not resp['success']:
                continue

            formatter = TopicContentFormatter(resp['data'])
            replys.append(formatter.format())

        return fill_topic_reply_list_object(replys)

    def get_topic_page_reply(self, boardname, topicid, page):
        """
        get part of replies for a specific topic

        5 replys per page, page 0 means get all replys
        """
        all_replys = self.get_topic_all_reply(boardname, topicid)
        page = int(page)
        if page == 0:
            return all_replys
        
        all_replys['replies'] = all_replys['replies'][5 * (page - 1): 5 * page]
        return all_replys

    def __add_post(self, post_type, boardname, topic_id, title, content, attach):
        '''
        Helper for adding post
        '''
        if attach:
            attach = StringIO.StringIO(attach)

        if post_type == 'reply':
            r = requests.post(add_post_site, cookies=self.cookie, data={'type': post_type, 'boardname': boardname, 
                'articleid': topic_id, 'title': title, 'content': content}, 
                files=({'attach': attach} if attach else None))
        elif post_type == 'new':
            r = requests.post(add_post_site, cookies=self.cookie, data={'type': post_type, 'boardname': boardname, 
                'title': title, 'content': content}, 
                files=({'attach': attach} if attach else None))
        elif post_type == 'update':
            r = requests.post(add_post_site, cookies=self.cookie, data={'type': post_type, 'boardname': boardname, 
                'articleid': topic_id, 'title': title, 'content': content}, 
                files=({'attach': attach} if attach else None))
        else:
            raise ValueError('Invalid post_type %s' % post_type)

        log_server('add_post %s: %s' % (post_type, r.text))
        # FIXME: Send a post with attachment will response 502 error
        #        Don't know why. ISSUE #10
        resp = r.json()
        if resp['success']:
            return {'id': resp['data']}
        return resp['code']

    def reply_topic(self, boardname, id, title, content, attachment=None):
        """
        reply a post
        """
        return self.__add_post('reply', boardname, id, title, content, attachment)

    def new_topic(self, boardname, title, content, attachment=None):
        '''
        New topic
        '''
        return self.__add_post('new', boardname, None, title, content, attachment)

    def update_post(self, boardname, id, title, content, attachment=None):
        '''
        update topic
        '''
        return self.__add_post('update', boardname, id, title, content, attachment)
        
    def del_post(self, boardname, id):
        """
        delete a post
        """
        r = requests.post(del_post_site, cookies=self.cookie, data={'boardname': boardname, 'filename': id})
        resp = r.json()
        if resp['success']:
            return True
        return resp['code']

    def get_post_content(self, boardname, postid):
        """
        get a specific post content according
        to post's id
        """
        r = requests.get(get_post_content_site, params={'boardname': boardname, 'filename': postid})
        resp = r.json()
        if resp['success']:
            formatter = TopicContentFormatter(resp['data'])
            return formatter.format()

        return resp['code']

    def get_topic_content(self, topic_id):
        return self.get_post_content(topic_id)

