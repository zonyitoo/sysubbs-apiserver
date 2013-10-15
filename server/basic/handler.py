# -*- coding:utf8 -*-

from flask import Blueprint

class Handler(object):
    """
    basic Handler class

    Handler is a class that in charge of part of API,
    it contains a flask.Blueprint object that makes
    Handler act as a submodule of Flask app
    """
    def __init__(self, name, url_prefix, app):
        """
        init Handler with a prefix

        Args:
            url_prefix (str): the url prefix used in register blueprint
            name (str): the name of this handler
            app (flask.Flask): the flask appliction object, used when register blueprint
        """
        self.blueprint = Blueprint(name, __name__)
        self.url_prefix = url_prefix
        self.app = app

    def register_handler(self):
        """
        register this handler

        Args:
            app (flask.Flask): the appliction object which this handler is
            registered for
        """
        self.add_all_view_functions()
        self.app.register_blueprint(self.blueprint, url_prefix=self.url_prefix)

    def add_view_func(self, rule, methods, func):
        """
        add a view function for specific rule

        Args:
            rule (str): the url rule, with Flask specification format
            methods (list or tuple): the http methods
            func (function): the function
        """
        self.blueprint.add_url_rule(rule=rule, view_func=func)

    def add_all_view_functions(self):
        """
        This is a helper method, you can add all your view functions
        here, ``register_handler`` will invoke this method before
        registering blueprint
        """
        pass
