import json

from server.basic import BasicFormatter

class CookieFormater(BasicFormatter):
    """
    CookieFormater, format cookie in this format:
    {'cookie': cookie}
    """
    def format(self):
        return dict(cookie=self.raw_data)

class UserFormatter(BasicFormatter):
    def format(self, server_resp):
        pass
