import json

from server.basic import BasicFormatter
from server.objects import fill_friend_object, fill_friends_list_object, \
        fill_board_object, fill_board_list_object, fill_user_info_object

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
        raw_friends_list = self.raw_data
        friends_list = []
        for friend in raw_friends_list:
            username = friend['id']
            alias = friend['exp']
            friends_list.append(fill_friend_object(username, alias))
        return fill_friends_list_object(friends_list)

class UserFavBoardFormatter(BasicFormatter):
    """
    UserFavBoardFormatter, format "jsbbs get user fav boards api
    return object as our board object"
    """
    def format(self):
        data = self.raw_data
        return fill_board_object(boardname=data['boardname'],
                description=data['title'], moderators=data['BM'],
                section_code=data['seccode'], total_posts=data['total'],
                last_post_time=data['lastpost'])

class UserFavBoardListFormatter(BasicFormatter):
    """
    UserFavBoardListFormatter, format "jsbbs get user fav boards api"
    return list as our board list object
    """
    def format(self):
        data = self.raw_data
        boards = []
        for b in data:
            board_formatter = UserFavBoardFormatter(json.dumps(b))
            boards.append(board_formatter.format())
        return fill_board_list_object(boards)

class UserInfoFormatter(BasicFormatter):
    """
    UserInfoFormatter, format the jsbbs user info object as our
    user info object
    """
    def format(self):
        data = self.raw_data
        gender = data['male']
        if gender:
            gender = "M"
        else:
            gender = "F"
        return fill_user_info_object(username=data['userid'], nickname=data['username'],
                life_value=data['life_value'], stay_time=data['stay'], gender=gender,
                signature=data['signature'], description=data['plan'], numposts=data['numposts'])
