import inspect

from functools import wraps
from server.basic.code import no_login


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

    def has_cookie(self):
        ret = hasattr(self, 'cookie')
        print "in has_cookie, ret=" + str(ret)
        return ret

#class CheckCookieMethod(object):
#    def __init__(self, func):
#        self.func = func
#
#    def __get__(self, obj, cls=None):
#        def wrapper(*args, **kwargs):
#            if not obj.has_cookie():
#                return no_login
#            ret = self.func(obj, *args, **kwargs)
#            return ret
#        return wrapper
#
#def add_cookie_check(exclude_methods=[]):
#    def decorated(cls):
#        def wrap():
#            for name, method in inspect.getmembers(cls, inspect.ismethod):
#                if name not in exclude_methods and not inspect.isclass(method.im_self):
#                    setattr(cls, name, CheckCookieMethod(method))
#            return cls
#        return wrap
#    return decorated

#def add_cookie_check(cls):
#     for name, method in inspect.getmembers(cls, inspect.ismethod):
#         if not inspect.isclass(method.im_self):
#             print name
#             setattr(cls, name, CheckCookieMethod(method))
#     return cls

#class CookieChecker(object):
#    def __init__(self, exclude_methods=[]):
#        self.exclude_methods = exclude_methods
#
#    def check(self, cls):
#        for name, method in inspect.getmembers(cls, inspect.ismethod):
#            if not inspect.isclass(method.im_self) and \
#                name not in self.exclude_methods and \
#                '__init__' != name and 'has_cookie' != name:
#                setattr(cls, name, CheckCookieMethod(method))
#        return cls
