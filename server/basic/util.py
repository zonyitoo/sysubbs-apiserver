import json

from flask import request

def get_json_post_data():
    info = request.get_json()
    if info:
        return info
    else:
        info = request.data
        info = json.loads(info)
        return info
