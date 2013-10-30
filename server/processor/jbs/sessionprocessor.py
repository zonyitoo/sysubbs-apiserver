import requests

from server.basic import BasicSessionProcessor
from urls import *
from server.basic.formatter import fill_fail_format, fill_success_format
from sessionformatter import SessionListFormatter

class SessionProcessor(BasicSessionProcessor):
    def get_session_list(self):
        """
        get all sessions

        Returns:
            session list object (dict) or
            err_code if fail
        """
        r = requests.get(url=get_session_site)
        resp = r.json()
        if resp['success']:
            raw_data = resp['data']
            formatter = SessionListFormatter(raw_data)
            return formatter.format()
        else:
            code = resp['code']
            return code
