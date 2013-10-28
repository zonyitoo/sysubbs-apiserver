__description__ = """
                  Handlers for each part of API
                  """

from server.logger import init_logger
from server.basic.auth import require_auth
init_logger()


def create_all_handlers(app):
    #from server.basic.handler import Handler
    import kaptan
    url_config = kaptan.Kaptan()
    url_config.import_config('handler/urls.yaml')

    import os
    handlers = []
    for cur, dire, files in os.walk('handler/%s' % app.config['USED_HANDLER']):
        handler_config = kaptan.Kaptan()
        if 'handlers.yaml' in files:
            handler_config.import_config('%s/%s' % (cur, 'handlers.yaml'))
        elif 'handlers.json' in files:
            handler_config.import_config('%s/%s' % (cur, 'handlers.json'))
        else:
            raise ValueError("Cannot find any handlers configuration file in %s" % cur)

        exec('import %s' % app.config['USED_HANDLER'])
        for hname, vals in handler_config.get().items():
            h = eval('%s(app)' % hname)
            h.__url_prefix__ = url_config.get('%s.url_prefix' % vals['role'])
            if vals.has_key('views'):
                for vname, vargs in vals['views'].items():
                    view_func = eval('h.%s' % vname)
                    try:
                        if url_config.get('%s.%s.require_auth' % (vals['role'], vargs['role'])):
                            view_func = require_auth(view_func)
                    except KeyError:
                        pass
                    h.add_view_func(rule=url_config.get('%s.%s.url' % (vals['role'], vargs['role'])), 
                            func=view_func, 
                            methods=tuple(url_config.get('%s.%s.methods' % (vals['role'], vargs['role']))))
            handlers.append(h)

        break

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
