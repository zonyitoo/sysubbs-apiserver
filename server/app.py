from flask import Flask

def init_app():
    app = Flask(__name__)

    return app

if __name__ == '__main__':
    import os
    app = init_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
