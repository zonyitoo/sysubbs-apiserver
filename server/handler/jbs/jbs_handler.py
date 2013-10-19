from flask import request

from server.basic.handler import Handler
from server.basic.auth import get_cookie_from_authorization

class jbsHandlerMixin(object):
    """
    jbsHandlerMixin, add cookie support for handler
    """

    def set_cookie(self):
        """
        set the cookie value for processor before request
        """
        if 'request_access_token' not in request.url and 'deliver_server_publickey' not in request.url:
            cookie = get_cookie_from_authorization()
            print "cookie is " + str(cookie)
            if cookie and hasattr(self.__processor__, 'set_cookie'):
                self.__processor__.set_cookie(cookie)

class jbsHandler(Handler, jbsHandlerMixin):
    """
    all handler use in jsbbs api must inherit this class
    """
    def __init__(self, *args, **kwargs):
        super(jbsHandler, self).__init__(*args, **kwargs)
        self.blueprint.before_request(self.set_cookie)
