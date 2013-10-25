import time
import base64
import json
import rsa
import StringIO

server_publickey = \
u"""
-----BEGIN RSA PUBLIC KEY-----
MBgCEQC+xlMZRSu5W1fw4DqAlk9NAgMBAAE=
-----END RSA PUBLIC KEY-----
"""
HOST = "http://127.0.0.1:5050"

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
