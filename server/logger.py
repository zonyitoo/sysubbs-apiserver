import logging
import logging.config

def init_logger():
    logging.config.fileConfig("logger.ini")

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
                'request': json.dumps(fake_request_arg),
                'response': json.dumps(fake_response),
                'apiname': '/user/login'
            }

    requestlog.debug('logger testing', extra=extra_log_msg)
