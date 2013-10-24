import json

from flask import request, make_response

from code import request_data_format_error
from formatter import fill_fail_format

def get_json_post_data():
    info = request.get_json()
    if info:
        return info
    elif request.data:
        info = request.data
        info = json.loads(info)
        return info
    elif request.form:
        info = dict(request.form)
        return info

def is_process_success(ret):
    if type(ret) is dict or ret is True:
        return True
    else:
        return False

def post_data_format_error():
    return make_response(fill_fail_format(err_code=request_data_format_error))
