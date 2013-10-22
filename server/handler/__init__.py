__description__ = """
                  Handlers for each part of API
                  """

from server.logger import init_logger
from flask import Blueprint
init_logger()


def create_all_handlers(app):
    #from server.basic.handler import Handler
    import kaptan
    url_config = kaptan.Kaptan()
    url_config.import_config('urls.yaml') 

    import os
    handlers = []
    for cur, dire, files in os.walk('.'):
        if cur == '.': continue

        handler_config = kaptan.Kaptan()
        if 'handlers.yaml' in files:
            handler_config.import_config(cur + 'handlers.yaml')
        elif 'handlers.ini' in files:
            handler_config.import_config(cur + 'handlers.ini')
        elif 'handlers.json' in files:
            handler_config.import_config(cur + 'handlers.json')
        elif 'handlers.conf' in files:
            handler_config.import_config(cur + 'handlers.conf')
        else:
            raise ValueError("Cannot find handlers configuration file in %s" % cur)

        for hname, vals in handler_config.get().items():
            exec('import %s' % hname)
            h = eval('%s(app)' % hname)
            h.__url_prefix__ = url_config.get('%s.url_prefix' % vals['role'])
            if vals.has_key('views'):
                for view in vals['views']:
                    h.add_url_rule(url_config.get('%s.%s' % (vals['role'], view['role'])), 
                            eval('h.%s' % view['name']), eval(view['methods']))
            handlers.append(h)

    return handlers

def register_api_handlers(app):
    """
    register all handlers

    Args:
        app (flask.Flask): the application object which this handler is registered for
    """
    handlers = create_all_handlers(app)
    for h in handlers:
        h.register_handler()
