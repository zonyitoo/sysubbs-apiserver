import logging
import logging.config

from flask import request

def init_logger():
    logging.config.fileConfig("logger.ini")

def log_request(request, response, level='debug', username='', api_addr='/'):
    extra_log_msg = {
                'clientip': request.remote_addr,
                'userid': username,
                'request': request,
                'response': response,
                'apiname': api_addr
            }
    requestlog = logging.getLogger('requestlog')
    log_func = getattr(requestlog, level)
    if log_func:
        log_func('handle %s' % api_addr, extra=extra_log_msg)

def log_server(msg, level='debug'):
    serverlog = logging.getLogger('serverlog')
    log_func = getattr(serverlog, level)
    if log_func:
        log_func(msg)

if __name__ == "__main__":
    print "Testing logger configuration"

    init_logger()
    root_logger = logging.getLogger('root')
    serverlog = logging.getLogger('serverlog')
    requestlog = logging.getLogger('requestlog')

    root_logger.debug('root debug_message')
    serverlog.debug('serverlog_debug_message')
    fake_request_arg = {
                'arg1': 'test arg1',
                'arg2': '1'
            }
    fake_response = {
                'err': False,
                'world': 'hello',
                'user' : {'name': 'Ragnarok', 'City': 'Mars'},
            }
    import json
    extra_log_msg = {
                'clientip': '127.0.0.1',
                'userid': '124567000111',
                'request': fake_request_arg,
                'response': fake_response,
                'apiname': '/user/login'
            }

    requestlog.debug('logger testing', extra=extra_log_msg)
