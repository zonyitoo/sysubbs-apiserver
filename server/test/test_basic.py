import time
import base64
import json
import rsa
import StringIO
import logging
logger = logging.getLogger()

server_publickey = \
u"""
-----BEGIN RSA PUBLIC KEY-----
MBgCEQC+xlMZRSu5W1fw4DqAlk9NAgMBAAE=
-----END RSA PUBLIC KEY-----
"""
HOST = "http://127.0.0.1:5050"

import sys
sys.path.append('..')

from server.app import init_app
app = init_app().test_client()

import kaptan
url_config = kaptan.Kaptan()
url_config.import_config('handler/urls.yaml')

def get_url_by_role(prefix, role):
    return url_config.get(prefix)['url_prefix'] + url_config.get('%s.%s' % (prefix, role))['url']

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

def get_request_header(access_token):
    data = {'access_token': access_token, "nounce": time.time()}
    data = json.dumps(data)

    data = __rsa128_encrypt_str(data, rsa.PublicKey.load_pkcs1(server_publickey))
    headers = {'Authorization': data}

    return headers

def save_binary_content(binary_content, out_filename):
    file_io = StringIO.StringIO(binary_content)
    new_file = open(out_filename, 'w')
    new_file.write(file_io.getvalue())
    new_file.close()
    file_io.close()

def get_binary_content(filename):
    f = open(filename)
    content = ''.join(f.readlines())
    f.close()
    return content

import unittest
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        from test_auth import *
        self.client = app        
        self.server_publickey, self.login_token = get_server_publickey()
        self.access_token, self.expire = get_access_token(self.server_publickey, self.login_token)

    def tearDown(self):
        from test_auth import *
        logger.info('Logout %s' % str(logout(self.access_token, self.server_publickey)))
