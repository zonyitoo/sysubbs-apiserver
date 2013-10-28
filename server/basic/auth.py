"""
Helper classes and methods for authentication

the login_token store in this format:
    "auth:login_token:[login_token_value]: {'client_publickey': '...'}"

    login_token will be expired in 120 minutes

the access_token store in this format:
    "auth:access_token:[access_token_value]: {
                    'client_publickey': '....',
                    'username': '...',
                    'cookies':cookie,
                    'nounce': 'timestamp'}"

    access_token will be expired in 30 days
"""
login_token_key_format = 'auth:login_token:[%s]'
access_token_key_format = 'auth:access_token:[%s]'

import uuid
import rsa
import redis
import json
import time
import base64

from requests.utils import cookiejar_from_dict, add_dict_to_cookiejar
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

def get_client_publickey_from_authorization():
    """
    get the client public key from Authorization (no encrypt)

    Returns:
        client_publickey (dict)
    """
    client_publickey = request.headers.get('Authorization', None)
    if not client_publickey:
        return None
    else:
        try:
            client_publickey = json.loads(client_publickey)
            if 'client_publickey' in client_publickey:
                return client_publickey.get('client_publickey')
            else:
                return None
        except:
            return None

def store_access_token(access_token, token_info, expireat=int(time.time()) + 2592000):
    """
    store the access_token and its value, the access_token will be
    expired in 30 days

    Args:
        access_token (str): the access_token
        token_info (dict): the token value
    """
    _key = access_token_key_format % access_token
    redis_instance.set(name=_key, value=json.dumps(token_info))
    redis_instance.expireat(_key, expireat)

def store_login_token(login_token, token_info):
    """
    store the login_token and its value
    the login_token will be expired in 120 minutes

    Args:
        login_token (str): the login_token
        token_info (dict): the token value
    """
    redis_instance.setex(name=login_token_key_format % login_token,
            time=7200, value=json.dumps(token_info))

def del_login_token(login_token):
    """
    delete the login_token

    Args:
        login_token (str): the login_token
    """
    redis_instance.delete(login_token_key_format % login_token)

def del_access_token(access_token):
    """
    delete the access_token

    Args:
        access_token (str): the access_token
    """

def get_login_token_value(login_token):
    return redis_instance.get(login_token_key_format % login_token)

def get_access_token_value(access_token):
    return redis_instance.get(access_token_key_format % access_token)

def get_cookie_from_access_token(access_token):
    access_token_val = redis_instance.get(access_token_key_format % access_token)
    if not access_token_val:
        return None
    access_token_val = json.loads(access_token_val)
    cookie = access_token_val.get('cookie', None)
    if cookie:
        return {'PHPSESSID': cookie}
    else:
        return None

def get_cookie_from_authorization():
    authorization = request.headers.get('Authorization', None)
    if authorization:
        client_data = decrypt_client_data(authorization)
        client_data = json.loads(client_data)
        access_token = client_data['access_token']
        return get_cookie_from_access_token(access_token)
    else:
        return None

def __rsa128_encrypt_str(data, public_key):
    data_remain = data
    result = ''
    while data_remain:
        cur = data_remain[:5]
        result += rsa.encrypt(cur, public_key)
        data_remain = data_remain[5:]

    result = base64.urlsafe_b64encode(str(result))

    return result

def __rsa128_decrypt_str(data, private_key):
    data = base64.urlsafe_b64decode(str(data))
    data_remain = data
    result = ''
    while data_remain:
        cur = data_remain[:16]
        result += rsa.decrypt(cur, private_key)
        data_remain = data_remain[16:]

    return result

def decrypt_client_data(data):
    """
    decrypt client post data, use server's private key

    Args:
        data (str): client post data

    Returns:
        the decrypted data
    """
    private_key = _app.config['SERVER_PRIVATE_KEY']
    return __rsa128_decrypt_str(data, private_key)

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
    return __rsa128_encrypt_str(data, public_key)

def get_access_token_and_nounce(authorization):
    """
    decrypt the access_token and nounce in Authorization header

    Args:
        authentication (str): the encrypted login_token

    Returns:
        the decrypted access_token and nounce,
        in this format:
            {'access_token': access_token, 'nounce': nounce, 'cookie': cookie}
    """
    #decoded_authorization = base64.urlsafe_b64decode(authorization)
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
    #decoded_authorization = base64.urlsafe_b64decode(authorization)
    user_info = get_access_token_and_nounce(authorization)
    access_token = user_info.get('access_token')
    if not access_token:
        return False
    nounce = user_info.get('nounce')
    if not nounce:
        return False
    try:
        nounce = float(nounce)
    except:
        return False
    store_user_info = redis_instance.get(access_token_key_format % access_token)
    if not store_user_info:
        return False
    store_user_info = json.loads(store_user_info)
    last_nounce = store_user_info.get('nounce')
    if not last_nounce:
        return False
    try:
        last_nounce = float(last_nounce)
    except:
        return False

    if nounce <= last_nounce:
        # the new nounce(timestamp) must bigger than last one
        return False
    else:
        # update new nounce
        store_user_info['nounce'] = nounce
        try:
            expireat = int(store_user_info['expire'])
        except:
            return False
        store_access_token(access_token, store_user_info, expireat)
        return True

def fail_auth():
    """
    return this when fail to auth
    """
    return make_response('Please login first', 401)

def fail_login_token_expired():
    """
    return this when login_token expired
    """
    return make_response('login_token has expired', 401)

def require_auth(func):
    """
    an auth decorator, if will be used in each view function
    that need login first
    the auth protocal: https://github.com/zonyitoo/sysubbs-apiserver/issues/1
    """
    @wraps(func)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization', None)
        if not auth:
            return fail_auth()
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
