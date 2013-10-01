import requests

from server.basic import BasicUserProcessor

class UserProcessor(BasicUserProcessor):
    """
    UserProcessor for jsbbs API
    """
    def login(self, username, password):
        pass

    def logout(self, cookie):
        pass

    def get_friends(self):
        pass

    def add_friend(self):
        pass

    def del_friend(self):
        pass

    def get_fav_boards(self):
        pass

    def add_fav_board(self):
        pass

    def del_fav_board(self):
        pass

    def get_user_info(self):
        pass

    def update_user_info(self):
        pass

    def get_user_avatar(self):
        pass
