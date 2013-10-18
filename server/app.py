from flask import Flask

from server.handler import register_api_handlers

def init_app():
    """
    this app is used for launch
    """
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    register_api_handlers(app)

    return app

def init_util_app():
    """
    this app is used for other files
    """
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    return app

if __name__ == '__main__':
    import os
    app = init_app()
    port = int(os.environ.get('PORT', 8000))
    app.run(host="0.0.0.0", port=port)
