__description__ = """
                  Handlers for each part of API
                  """

from server.logger import init_logger
init_logger()

from server.basic.handler import Handler

def create_all_handlers(app):
    from jbs import *
    handlers = []
    for cls in Handler.__subclasses__():
        h = cls(app)
        handlers.append(h)
    #login_handler = LoginHandler('login', '/login', app)
    #handlers.append(login_handler)

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
