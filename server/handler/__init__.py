__description__ = """
                  Handlers for each part of API
                  """

from server.logger import init_logger
init_logger()


def create_all_handlers(app):
    #from server.basic.handler import Handler
    from jbs import *
    from jbs.jbs_handler import jbsHandler
    handlers = []
    for cls in jbsHandler.__subclasses__():
        h = cls(app)
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
