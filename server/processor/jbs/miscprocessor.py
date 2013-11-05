import requests

from server.basic.formatter import fill_fail_format, fill_success_format
from server.basic.processor import BasicProcessor
from jbsprocess import jbsProcessorMixin
from miscformatter import TopicFormatter, TopicListFormatter

class MiscProcessor(BasicProcessor, jbsProcessorMixin):
    def get_my_topic(self):
        """
        get my topics

        Returns:
            Board Topic List Object
        """
        r = requests.get(get_my_topic_site, cookies=self.cookie)
        resp = r.json()
        items = resp['items']

        topics = []
        for topic in items:
            topic_id = topic['topicid']
            t = self.__get_first_post_by_topic_id(topic_id)
            t = TopicFormatter(t).format()
            topics.append(t)

        formatter = TopicListFormatter(topics)
        return formatter.format()

    def get_new_topic(self, offset=0):
        """
        get the newest topics

        Returns:
            Board List Object
        """
        r = requests.get(get_new_topic_site, params={'offset': offset})
        resp = r.json()

        items = resp['items'].values()
        topics = []
        for topic in items:
            topic_id = topic['topicid']
            t = self.__get_first_post_by_topic_id(topic_id)
            t = TopicFormatter(topic).format()
            topics.append(t)

        formatter = TopicListFormatter(topics)
        return formatter.format()

    def __get_first_post_by_topic_id(self, topic_id):
        """
        get the first post according to the topic id
        return a board_topic_object
        """
        r = requests.get(get_first_post_by_topicid_site, params={'filename': '', 'boardname': '', 'topicid': topic_id})
        resp = r.json()
        if resp['data']:
            return resp['data']
        else:
            return None
