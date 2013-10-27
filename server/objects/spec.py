"""
API objects specifications and helper methods
"""
"""
friends api
"""
def fill_friend_object(username, nickname):
    """
    Friend object:
        {'username': username, 'nickname': nickname}

    Returns:
        friend_object (dict)
    """
    return dict(username=username, nickname=nickname)

def fill_friends_list_object(friends_list):
    """
    in get_friends api
    Friends list object:
        {'friends': [friend_object, ...]}
    Returns:
        friends_list_object (dict)
    """
    return dict(friends=friends_list)

def fill_board_object(boardname="", description="", moderators=[], section_code="",
        total_posts=0, last_post_time=0):
    """
    Board object:
        {'boardname': boardname, 'description': description,
        'moderators': [m1username, m2....], 'section_code': code,
        'total_posts': total_posts_num, 'last_post_time': timestamp}
    """
    return dict(boardname=boardname, description=description, moderators=moderators, section_code=section_code,
            total_posts=total_posts, last_post_time=last_post_time)

def fill_board_list_object(board_list):
    """
    Board list object:
        {"boards": ['board object', ...]}
    """
    return dict(boards=board_list)

def fill_user_info_object(username="", nickname="", life_value=0, stay_time="",
        gender="M", signature="", description="", numposts=0):
    """
    User info object
    {'username': username, 'nickname': nickname, 'life_value': value, 'stay_time': time,
        'gender': M or F, 'signature': signature, 'description': description,
         'numposts': numposts}
    """
    return dict(username=username, nickname=nickname, life_value=life_value, stay_time=stay_time,
            gender=gender, signature=signature, description=description, numposts=numposts)

