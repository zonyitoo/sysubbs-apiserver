import json

from flask import request, make_response

from code import request_data_format_error

def get_json_post_data():
    info = request.get_json()
    if info:
        return info
    else:
        info = request.data
        info = json.loads(info)
        return info

def is_process_success(ret):
    if ret is dict or ret is True:
        return True
    else:
        return False

def post_data_format_error():
    return make_response(fill_fail_format(err_code=request_data_format_error))
