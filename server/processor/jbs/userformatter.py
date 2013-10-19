import json

from server.basic import BasicFormatter
from server.basic.formatter import fill_friend_object, fill_friends_list_object

class CookieFormater(BasicFormatter):
    """
    CookieFormater, format cookie in this format:
    {'cookie': cookie}

    Returns:
        the new cookie object (dict), in this format:
        {'cookie': cookie}
    """
    def format(self):
        return dict(cookie=self.raw_data)


class FriendsListFormatter(BasicFormatter):
    """
    FriendsListFormatter, format jsbbs API get_friend api

    the jsbbs response in this format:
        [{"id": username, "exp": exp}, ...]

    Returns:
        friends_list (dict): in this format:
        {friends: [friend_object, ...]}
    """
    def format(self):
        raw_friends_list = json.loads(self.raw_data)
        friends_list = []
        for friend in raw_friends_list:
            username = friend['username']
            alias = friend['exp']
            friends_list.append(fill_friend_object(username, alias))
        return fill_friends_list_object(friends_list)
