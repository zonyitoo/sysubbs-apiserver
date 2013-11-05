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
                )

class TopicListFormatter(BasicFormatter):
    def format(self):
        return fill_board_topic_list_object(topics=self.raw_data)
