# -*- coding:utf8 -*-

from flask import Blueprint

class Handler(object):
    """
    basic Handler class

    Handler is a class that in charge of part of API,
    it contains a flask.Blueprint object that makes
    Handler act as a submodule of Flask app
    """

    """
    each subclass of Handler must have this two properties:
    __handler_name__ (str): the name of this handler
    __url_prefix__ (str): the url_prefix used in register blueprint
    __processor__ (Processor): the processor for this Handler
    """
    __handler_name__ = 'handler'
    __processor__ = None

    def __init__(self, app):
        """
        init Handler with a prefix

        Args:
            app (flask.Flask): the flask appliction object, used when register blueprint
        """
        self.blueprint = Blueprint(self.__handler_name__, __name__)
        self.app = app

    def register_handler(self):
        """
        register this handler

        Args:
            app (flask.Flask): the appliction object which this handler is
            registered for
        """
        self.app.register_blueprint(self.blueprint, url_prefix=self.__url_prefix__)

    def add_view_func(self, rule, methods, func):
        """
        add a view function for specific rule

        Args:
            rule (str): the url rule, with Flask specification format
            methods (list or tuple): the http methods
            func (function): the function
        """
        self.blueprint.add_url_rule(rule=rule, view_func=func, methods=list(methods))
