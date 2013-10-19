from functools import wraps

class jbsProcessorMixin(object):
    """
    jbsProcessorMixin, add cookie support for processor
    """
    def set_cookie(self, cookie):
        """
        set the cookie for the processor
        it must be call before operation

        Args:
            cookie (cookiejar): the cookie
        """
        self.cookie = cookie
