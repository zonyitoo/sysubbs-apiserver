"""
test session api
"""

import requests
import json
from base import get_session_site

def get_sessions():
    r = requests.get(url=get_session_site)
    return r.json()

if __name__ == '__main__':
    resp = get_sessions()
    success = resp['success']
    data = resp['data']
    print "get_sessions, success: %s\n data: %s" % (success, json.dumps(data, sort_keys=True, indent=4))
