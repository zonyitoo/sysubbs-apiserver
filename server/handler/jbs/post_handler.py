from server.basic.util import get_json_post_data, is_process_success, post_data_format_error
from server.basic.handler import Handler
from server.basic.formatter import fill_fail_format, fill_success_format
from server.processor.jbs.postprocessor import PostProcessor
from jbs_handler import jbsHandler
from server.logger import log_server, log_request
from server.basic.auth import *
from server.basic.code import *
import base64

class PostHandler(jbsHandler):
    __handler_name__ = 'jbspost'
    __processor__ = PostProcessor()

    def get_board_topics_list(self, offset, boardname):
        '''
        Get topic list in a specific board, which is older than the topic with `start` index
        param: 
            start: the latest board index
            boardname: board's name
        methods: GET
        response:
            A list of topics' header infomation. Max 20.
        '''
        ret = self.__processor__.get_board_topics_list(offset, boardname)
        log_request(api_addr='get_board_topics_list', 
                request={'boardname': boardname}, response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def get_topic_all_reply(self, boardname, topicid):
        '''
        Get all reply to a specific topic
        param:
            boardname: board's name
            topicid: topic's id
        methods: GET
        response:
            A list of replies (Post objects)
        '''
        ret = self.__processor__.get_topic_all_reply(boardname, topicid)
        log_request(api_addr='get_topic_all_reply', 
                request={'boardname': boardname, 'topic_id': topicid}, 
                response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def get_topic_page_reply(self, boardname, topicid, page):
        '''
        Get replies page by page. 5 replies per page.
        param:
            boardname: board's name
            topicid: topic's id
            page: >= 0, 0 means get all replies. Pages starts from 1.
        methods: GET
        response:
            A list of replies (Post objects)
        '''
        ret = self.__processor__.get_topic_page_reply(boardname, topicid, page)
        log_request(api_addr='get_topic_all_reply', 
                request=dict(boardname=boardname, topicid=topicid, page=page),
                response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def get_post_info(self, boardname, topicid):
        '''
        Get detail information of a specific `post`. A `post` means a `topic` or a `reply`. 
        param:
            boardname: board's name
            topicid: `post`'s id
        methods: GET
        response:
            A post object
        '''
        ret = self.__processor__.get_post_content(boardname, topicid)
        log_request(api_addr='get_post_info', 
                request=dict(boardname=boardname, topicid=topicid),
                response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def reply_topic(self):
        '''
        Reply a topic or a reply.
        methods: POST
        Post data format:
        {
            'boardname': board's name,
            'id': `id` of a topic that you want to reply,
            'title': title,
            'content': content,
            'attachment': attachment (attachment should be binary encoded by base64),
        }
        response: if success, it will return a `id` of reply in this format
        {
            'id': reply's id
        }
        '''
        data = get_json_post_data()
        if not data or 'boardname' not in data\
            or 'id' not in data\
            or 'title' not in data\
            or 'content' not in data:
                return post_data_format_error()

        try:
            if 'attachment' in data and data['attachment']:
                data['attachment'] = base64.decodestring(data['attachment'])
        except:
            log_request(api_addr='reply_topic', level='error', request=data)
            return post_data_format_error()

        ret = self.__processor__.reply_topic(**data)
        log_request(api_addr='reply_topic', request=data, response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def new_topic(self):
        '''
        New topic.
        methods: POST
        Post data format:
        {
            'boardname': board's name,
            'title': title,
            'content': content,
            'attachment': attachment (attachment should be binary encoded by base64),
        }
        response: if success, it will return the `id` of new post in this format
        {
            'id': `id` of new post
        }
        '''
        data = get_json_post_data()
        if not data or 'boardname' not in data\
            or 'title' not in data\
            or 'content' not in data:
                return post_data_format_error()

        try:
            if 'attachment' in data and data['attachment']:
                data['attachment'] = base64.decodestring(data['attachment'])
        except:
            log_request(api_addr='new_topic', level='error', request=data)
            return post_data_format_error()

        ret = self.__processor__.new_topic(**data)
        log_request(api_addr='new_topic', request=data, response=ret)

        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def update_post(self):
        '''
        Updata post
        methods: POST
        Post data format:
        {
            'boardname': board's name,
            'id': post's `id`,
            'title': title,
            'content': content,
            'attachment': attachment (attachment should be binary encoded by base64),
        }
        response: if success, it will return the `id` of post in this format
        {
            'id': `id` of post
        }
        '''
        data = get_json_post_data()
        if not data or 'boardname' not in data\
            or 'id' not in data\
            or 'title' not in data\
            or 'content' not in data:
                return post_data_format_error()
    
        try:
            if 'attachment' in data and data['attachment']:
                data['attachment'] = base64.decodestring(data['attachment'])
        except:
            log_request(api_addr='update_post', level='error', request=data)
            return post_data_format_error()

        ret = self.__processor__.update_post(**data)
        log_request(api_addr='update_post', request=data, response=ret)
        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))

    def delete_post(self):
        '''
        Delete a post.
        methods: POST
        post data format
        {
            'boardname': board's name,
            'id': the `id` of the post to be deleted
        }
        response: success or fail
        '''
        data = get_json_post_data()
        if not data or 'boardname' not in data\
            or 'id' not in data:
                return post_data_format_error()

        ret = self.__processor__.del_post(**data)
        log_request(api_addr='delete_post', request=data, response=ret)

        if is_process_success(ret):
            return make_response(fill_success_format(ret))
        else:
            return make_response(fill_fail_format(err_code=ret))


