from server.basic import BasicFormatter
from server.objects.spec import *

class TopicListFormatter(BasicFormatter):
    '''
    TopicListFormatter, format jsbbs API get_board_posts api

    the jsbbs response in this format
        [topic_title, topic_title, ...]

    Response:
        topic_list: topic_list_object in this format
        { 'topics': [...] }
    '''
    def format(self):
        topics = [
                fill_board_topic_object(
                        offset=topic['index'],
                        id=topic['filename'],
                        ownerid=topic['owner'],
                        title=topic['title'],
                        total_reply=topic['total_reply'],
                        unread=bool(topic['unread']),
                        post_time=topic['update']
                    )
                for topic in self.raw_data
            ]

        return fill_board_topic_list_object(topics)

class TopicContentFormatter(BasicFormatter):
    '''
    TopicContentFormatter, format jsbbs API get_post_content api
    
    the jsbbs response in this format
        { topic_content_object }

    Response:
        topic_content_object
    '''
    def format(self):
        data = self.raw_data
        return fill_topic_content_object(
                    offset=data['index'],
                    id=data['filename'],
                    ownerid=data['userid'],
                    ownername=data['username'],
                    title=data['title'],
                    boardname=data['board'],
                    post_time=data['post_time'],
                    content=data['rawcontent'],
                    signature=data['rawsignature'],
                    bbsname=data['bbsname'],
                    perm_del=bool(data['perm_del']),
                    attachments=[
                            fill_post_attachment_object(
                                    id=ah['filename'],
                                    origname=ah['origname'],
                                    mimetype=ah['desc'],
                                    filetype=ah['filetype'],
                                    post_id=ah['articleid'],
                                    link='http://bbs.sysu.edu.cn' + ah['link'],
                                )
                            for ah in data['ah']
                        ]
                )
