import os
import rsa

HERE = os.path.dirname(__file__)
DEBUG = True
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

SERVER_PUBLIC_KEY = rsa.PublicKey.load_pkcs1(
u"""
-----BEGIN RSA PUBLIC KEY-----
MBgCEQC+xlMZRSu5W1fw4DqAlk9NAgMBAAE=
-----END RSA PUBLIC KEY-----
""")
SERVER_PRIVATE_KEY = rsa.PrivateKey.load_pkcs1(
u"""
-----BEGIN RSA PRIVATE KEY-----
MGMCAQACEQC+xlMZRSu5W1fw4DqAlk9NAgMBAAECEQCPMT9YXWH3QO6GkB0gF/fh
AgkOZpsvl0rA1wkCCA0/XFIWCSMlAgkD7XQRrL+UjJECCANIlSVzeMhRAgkJBkIV
BvuNBEA=
-----END RSA PRIVATE KEY-----
""")
