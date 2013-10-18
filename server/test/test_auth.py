import requests
import rsa
import json
import time
import base64

client_publickey = rsa.PublicKey.load_pkcs1(u'-----BEGIN RSA PUBLIC KEY-----\nMBgCEQCzxvEyRJXuwye7pJ/CO6yDAgMBAAE=\n-----END RSA PUBLIC KEY-----\n')
client_privatekey = rsa.PrivateKey.load_pkcs1(u'-----BEGIN RSA PRIVATE KEY-----\nMGICAQACEQCzxvEyRJXuwye7pJ/CO6yDAgMBAAECEAtsJH8RJIWaVzsglJjPgSEC\nCQvWDmTO3FPHXwIIDzBVuDiHIV0CCQSEUcXis249XQIIC7XJMMmsLSUCCQqYaBIP\nXS5orA==\n-----END RSA PRIVATE KEY-----\n')

client_publickey_str = u'-----BEGIN RSA PUBLIC KEY-----\nMBgCEQCzxvEyRJXuwye7pJ/CO6yDAgMBAAE=\n-----END RSA PUBLIC KEY-----\n'

HOST = "http://127.0.0.1:5000"

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

def get_server_publickey():
    headers = {'Authorization': json.dumps({'client_publickey': client_publickey_str})}
    resp = requests.get(HOST + "/auth" + "/deliver_server_publickey/", headers=headers)

    authorization = resp.headers.get('Authorization')
    if authorization:
        authorization = json.loads(authorization)
        server_publickey = authorization['server_publickey']
        login_token = authorization['login_token']

        #print server_publickey
        #print login_token
        return server_publickey, login_token

def get_access_token(server_publickey, login_token):
    data = {'username': 'okone', 'password': '8612001', 'login_token': login_token, 'nounce': int(time.time())}
    data = json.dumps(data)
    data = __rsa128_encrypt_str(data, rsa.PublicKey.load_pkcs1(server_publickey))
    headers = {'Authorization': data}

    resp = requests.get(HOST + "/auth" + "/request_access_token/", headers=headers)

    authorization = resp.headers.get('Authorization')
    if authorization:
        authorization = __rsa128_decrypt_str(authorization, client_privatekey)
        authorization = json.loads(authorization)
        access_token = authorization['access_token']
        expire = int(authorization['expire'])

        return access_token, expire


if __name__ == '__main__':
    server_publickey, login_token = get_server_publickey()
    access_token, expire = get_access_token(server_publickey, login_token)

    print """
    server_publickey:\n %s\n
    login_token: %s\n
    access_token: %s\n
    expire: %s
    """ % (server_publickey, login_token, access_token, expire)
