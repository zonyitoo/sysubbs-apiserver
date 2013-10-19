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
