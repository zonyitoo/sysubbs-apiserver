# -*- coding:utf8 -*-

import uuid
import rsa

class Handler(object):

    """
    Handler base class

    Handler is for restructuring data from client,
    and retrieving data from a specific Processor.
    """

    def __init__(self, server_publickey, server_privatekey, redis_instance):
        self.server_publickey = server_publickey
        self.server_privatekey = server_privatekey
        self.redis_instance = redis_instance

    def get_server_publickey(self, client_publickey):
        """
        Get Server Public key.

        @param:
        client_publickey: Client's public key, in PKCS#1 format

        @return
        {
            "server_publickey": "...",
            "login_token": "...",
        }
        """
        login_token = str(uuid.uuid1())
        while self.redis_instance.get(login_token):
            login_token = str(uuid.uuid1())

        self.redis_instance.set(login_token, client_publickey)
        self.redis_instance.expire(login_token, 120)

        response = {
                'server_publickey': self.server_publickey.save_pkcs1(),
                'login_token': login_token,
            }

        return response

    def authorization_encrypt(self, login_token, message):
        """
        Encrypt message with Client_PublicKey
        """

        client_publickey = self.redis_instance.get(login_token)

        if not client_publickey:
            return None

        rsa_pub = rsa.PublicKey.load_pkcs1(client_publickey)
        return rsa.encrypt(rsa_pub, message)
        
    def authorization_decrypt(self, message):
        """
        Decrypt message
        
        @throw rsa.DecryptionError
        """

        return rsa.decrypt(self.server_privatekey, message)

