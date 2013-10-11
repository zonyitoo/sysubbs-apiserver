import requests

from base import *

def get_errcode():
    r = requests.get(url=get_errcode_site)
    return r.json()

if __name__ == '__main__':
    print get_errcode()
