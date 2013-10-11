#-*- coding: urtf8 -*-
"""
Helper classes and methods for authentication
"""

import uuid
import rsa
import redis

from functools import wraps
from flask import request, Response, make_response

class RedisInstance(object):
    """
    helper class to create a singlton redis instance
    among the project

    usage: redis_instance = RedisInstance.create_instance().r
    """
    def __init__(self, host='localhost', port=6379):
        self._pool = redis.ConnectionPool(host=host, port=port)
        #self._r = redis.Redis(connection_pool=self._pool)

    @classmethod
    def create_instance(cls):
        if hasattr(cls, '__instance'):
            return cls.__instance
        else:
            cls.__instance = cls()
            return cls.__instance

    @property
    def r(self):
        """
        return an active redis client
        """
        #return self._r
        return redis.Redis(connection_pool=self._pool)

redis_instance = RedisInstance.create_instance().r

def gen_server_public_key(username, password):
    """
    generate a server public key for a user

    Args:
        username (str): username
        password (str): password

    Returns:
        the server public key
    """
    pass

def get_user_info_from_authorization(authorization):
    """
    decrypt the login_token in Authorization header

    Args:
        authentication (str): the encrypted login_token

    Returns:
        the decrypted login_token
    """
    pass

def check_auth(authorization):
    """
    check if user info is valid

    Args:
        authentication (str): the login_token in Authorization header, use RSA encrypt
    Returns:
        True, if auth succes or False if fail
    """
    pass

def fail_auth():
    """
    return this when fail to auth
    """
    return make_response('Please login first', 401)

def require_auth(func):
    """
    an auth decorator, if will be used in each view function
    that need login first
    the auth protocal: https://github.com/zonyitoo/sysubbs-apiserver/issues/1
    """
    @wraps(func)
    def decorated(*args, **kwargs):
        auth = request.authentication
        if not check_auth(auth):
            return fail_auth()
        return func(*args, **kwargs)
    return decorated
