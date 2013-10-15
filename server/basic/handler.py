# -*- coding:utf8 -*-

import uuid
import rsa
import redis

from flask import Blueprint

class Handler(object):
    """
    basic Handler class

    Handler is a class that in charge of part of API,
    it contains a flask.Blueprint object that makes
    Handler act as a submodule of Flask app
    """
    def __init__(self, name, url_prefix):
        """
        init Handler with a prefix

        Args:
            url_prefix (str): the url prefix used in register blueprint
            name (str): the name of this handler
        """
        self.blueprint = Blueprint(name, __name__)
        self.url_prefix = url_prefix

    def register_handler(self, app):
        """
        register this handler

        Args:
            app (Flask): the appliction object which this handler is
            registered for
        """
        app.register_blueprint(self.blueprint, url_prefix=self.url_prefix)

