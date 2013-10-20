"""
Basic classes for the Processor
"""


class Processor(object):
    """
    ~~~~
    Basic Processor class
    Processor is used to retrieve data from the server
    and format it in a correctly api format(only contain 'data' part and is a dict object)
    if request fail, it only return the error code,
    and pass to Handler the process this error code
    """
    def __init__(self):
        pass

class BasicSessionProcessor(Processor):
    """
    BasicSessionProcessor, used to get session infomation
    """
    def get_session_list(self):
        raise NotImplementedError()

class BasicUserProcessor(Processor):
    """
    BasicUserProcessor, used to register, login, logout, get/update user's info
    """
    def register(self):
        """
        register a new user
        """
        raise NotImplementedError()

    def login(self):
        """
        login
        """
        raise NotImplementedError()

    def logout(self):
        """
        logout
        """
        raise NotImplementedError()

    def get_friends(self):
        """
        get friends list
        """
        raise NotImplementedError()

    def add_friend(self):
        """
        make a new friend
        """
        raise NotImplementedError()

    def del_friend(self):
        """
        delete a friend :(
        """
        raise NotImplementedError()

    def get_fav_boards(self):
        """
        get user's favorite boards list
        """
        raise NotImplementedError()

    def add_fav_board(self):
        """
        add a new favorite board
        """
        raise NotImplementedError()

    def del_fav_board(self):
        """
        delete a favorite board
        """
        raise NotImplementedError()

    def get_user_info(self):
        """
        retrieve the other user's info or the user himself info
        """
        raise NotImplementedError()

    def update_user_info(self):
        """
        update a user's info
        """
        raise NotImplementedError()

    def update_user_avatar(self):
        """
        update user's avatar
        """
        raise NotImplementedError()

    def get_user_avatar(self):
        """
        get user's avatar
        """
        raise NotImplementedError()

class BasicBoardProcessor(Processor):
    """
    BasciBoardProcessor, used to retrieve boards' information
    """
    def get_all_boardname(self):
        """
        retrieve all boards' name
        """
        raise NotImplementedError()

    def get_all_boards_info(self):
        """
        get all boards' information
        """
        raise NotImplementedError()

    def get_board_info(self):
        """
        get a specfic board information
        """
        raise NotImplementedError()

    def clear_board_unread(self):
        """
        clear the unread marks for a specific board
        """
        raise NotImplementedError()

class BasicPostProcessor(Processor):
    """
    BasicPostProcessor, used to get/set posts' information
    """
    def get_board_topics_list(self):
        """
        get a specific board's topic list
        """
        raise NotImplementedError()

    def get_topic_all_reply(self):
        """
        get a specific topic's all replies
        """
        raise NotImplementedError()

    def get_topic_page_reply(self):
        """
        get part of replies for a specific topic
        """
        raise NotImplementedError()

    def reply_topic(self):
        """
        reply a post
        """
        raise NotImplementedError()

    def del_post(self):
        """
        delete a post
        """
        raise NotImplementedError()

class BasicMailProcess(Processor):
    def get_mailbox_info(self):
        """
        get the mailbox's information, for example,
        the number of mails, total size, used size
        """
        raise NotImplementedError()

    def get_mail_list(self):
        """
        get the mail list
        """
        raise NotImplementedError()

    def get_mail_info(self):
        """
        get the specific mail's information
        """
        raise NotImplementedError()

    def send_mail(self):
        """
        send mail! =w=
        """
        raise NotImplementedError()

    def del_mail(self):
        """
        delete a mail :(
        """
        raise NotImplementedError()
