import locale
import datetime
import time

from server.basic.formatter import BasicFormatter
from server.objects.spec import fill_board_topic_object, fill_board_topic_list_object

class TopicFormatter(BasicFormatter):
    """
    MyTopicFormatter, format raw data to board_topic_object
    """
    def format(self):
        return fill_board_topic_object(offset=0,
                id=self.raw_data['filename'],
                ownerid=self.raw_data['author'],
                title=self.raw_data['title'],
                total_reply=self.raw_data['replynum'],
                unread=False,
                post_time=format_time(self.raw_data['posttime'])
                )

class TopicListFormatter(BasicFormatter):
    def format(self):
        return fill_board_topic_list_object(topics=self.raw_data)

def format_time(raw_time):
    """
    format 2013-10-25 23:00:12 into timestamp
    """
    locale.setlocale(locale.LC_TIME, "en_US.UTF8")
    eng_datetime = datetime.datetime.strptime(t, "%Y-%b-%d %H:%M:%S")
    return time.mktime(eng_datetime.timetuple())
