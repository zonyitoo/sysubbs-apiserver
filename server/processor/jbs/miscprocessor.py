import requests

from server.basic.formatter import fill_fail_format, fill_success_format
from server.basic.processor import BasicProcessor
from jbsprocess import jbsProcessorMixin

class MiscProcessor(BasicProcessor, jbsProcessorMixin):
    def get_my_topic(self):
        """
        get my topics
        """
        r = requests.get(get_my_topic_site, cookies=self.cookie)
        pass

    def get_new_topic(self, offset):
        """
        get the newest topics
        """
        pass

    def __get_first_post_by_topic_id(self, topic_id):
        """
        get the first post according to the topic id
        return a board_topic_object
        """
        pass
