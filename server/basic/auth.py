"""
Helper classes and methods for authentication

the login_token store in this format:
    "auth:login_token:[login_token_value]: {'client_publickey': '...'}"

the access_token store in this format:
    "auth:access_token:[access_token_value]: {
                    'client_publickey': '....',
                    'username': '...',
                    'cookies':cookie}"
"""
login_token_key_format = 'auth:login_token:[%s]'
access_token_key_format = 'auth:access_token:[%s]'

import uuid
import rsa
import redis
import json
import time

from functools import wraps
from flask import request, Response, make_response
from server.app import init_util_app

_app = init_util_app()

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

def store_access_token(access_token, token_info):
    """
    store the access_token and its value, the access_token will
    expired in 30 days

    Args:
        access_token (str): the access_token
        token_info (dict): the token value
    """
    redis_instance.setex(access_token_key_format % access_token, 2592000, json.dumps(token_info))

def store_login_token(login_token, token_info):
    """
    store the login_token and its value
    the login_token will expired in 120 minutes

    Args:
        login_token (str): the login_token
        token_info (dict): the token value
    """
    redis_instance.setex(login_token_key_format % login_token, 7200, json.dumps(token_info))

def decrypt_client_data(data):
    """
    decrypt client post data, use server's private key

    Args:
        data (str): client post data

    Returns:
        the decrypted data
    """
    private_key = _app.config['SERVER_PRIVATE_KEY']
    return rsa.decrypt(data, private_key)

def encrypt_data_by_client_publickey(data, client_publickey):
    """
    encrypt data used client public key

    Args:
        data (str): the data to encrypt
        client_publickey (str): the client public key in pkcs#1 format

    Returns:
        the encrypted data
    """
    public_key = rsa.PublicKey.load_pkcs1(client_publickey)
    return rsa.encrypt(data, public_key)

def get_access_token_and_nounce(authorization):
    """
    decrypt the access_token and nounce in Authorization header

    Args:
        authentication (str): the encrypted login_token

    Returns:
        the decrypted access_token and nounce,
        in this format:
            {'access_token': access_token, 'nounce': nounce}
    """
    client_decrypeted_data = decrypt_client_data(authorization)
    client_info = json.loads(client_decrypeted_data)
    return client_info

def check_auth(authorization):
    """
    check if user info is valid

    Args:
        authentication (str): the  Authorization header, use RSA encrypt
    Returns:
        True, if auth succes or False if fail
    """
    user_info = get_access_token_and_nounce(authorization)
    access_token = user_info.get('access_token')
    if not access_token:
        return False
    nounce = user_info.get('nounce')
    if not nounce:
        return False

    store_user_info = redis_instance.get(access_token_key_format % access_token)
    if not store_user_info:
        return False

    current_timestamp = int(time.time())
    # 3 minutes
    if int(nounce) > current_timestamp or current_timestamp - int(nounce) > 120:
        return False

    return True
    
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


def gen_login_token():
    """
    generate a new login_token

    Returns:
        a new login_token (str)
    """
    login_token = str(uuid.uuid1())
    while redis_instance.get(login_token_key_format % login_token):
        login_token = str(uuid.uuid1())
    return login_token

def query_client_public_key(login_token):
    """
    query client public key according to the login_token

    Args:
        login_token (str): the login_token

    Returns:
        the client public key, if not exist, return None
    """
    login_token_value = redis_instance.get(login_token_key_format % login_token)
    if login_token_value:
        login_token_value = json.loads(login_token_value)
        return login_token_value.get('client_publickey')
    return None

def gen_access_token():
    """
    generate a new access_token

    Returns:
        a new access_token (str)
    """
    access_token = str(uuid.uuid1())
    while redis_instance.get(access_token_key_format % access_token):
        access_token = str(uuid.uuid1())
    return access_token
