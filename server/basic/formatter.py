import json

from flask.json import jsonify

class BasicFormatter(object):
    """
    Basic Formatter classes for the data retrieve from the server
    to format data into uniform data json object
    output format:
    {success: true, data} or
    {success: false, errCode: errCode, errMsg: errMsg}
    """
    def __init__(self, raw_data):
        if type(raw_data) is str:
            try:
                self.raw_data = json.loads(raw_data)
            except:
                self.raw_data = raw_data
        else:
            self.raw_data = raw_data


    def format(self):
        """
        format the raw_data into the specif json object,
        it must return a dict object
        """
        raise NotImplementedError()

def fill_success_format(data_object={}):
    """
    return the success case api format:
    {'success': True, 'data': data_object}
    the data_object may be a json object or an array
    """
    if data_object:
        return json.dumps(dict(success=True, data=data_object))
    else:
        return json.dumps(dict(success=True))

def fill_fail_format(err_msg='', err_code=000):
    """
    return the fail case api format:
    {'success': True, 'errMsg': errMsg, 'errCode': errCode}
    """
    if err_msg:
        return json.dumps(dict(success=False, errMsg=err_msg, errCode=err_code))
    else:
        return json.dumps(dict(success=False, errCode=err_code))

"""
API objects specifications and helper methods
"""
"""
friends api
"""
def fill_friend_object(username, alias):
    """
    Friend object:
        {'username': username, 'alias': alias}

    Returns:
        friend_object (dict)
    """
    return dict(username=username, alias=alias)

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
