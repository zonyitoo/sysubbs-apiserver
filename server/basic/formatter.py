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
        format the raw_data into the specif json object
        """
        raise NotImplementedError()

def fill_success_format(data_object={}):
    """
    return the success case api format:
    {'success': True, 'data': data_object}
    the data_object may be a json object or an array
    """
    return json.dumps(dict(success=True, data=data_object))

def fill_fail_format(err_msg='', err_code=000):
    """
    return the fail case api format:
    {'success': True, 'errMsg': errMsg, 'errCode': errCode}
    """
    return json.dumps(dict(success=False, errMsg=err_msg, errCode=err_code))
