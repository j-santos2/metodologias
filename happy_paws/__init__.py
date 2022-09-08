import logging
from os import getenv

from flask import Flask

app = Flask(__name__)

def create_app():
    app.logger.setLevel(logging.INFO)

    from happy_paws.blueprints.index_bp import index
    from happy_paws.blueprints.auth_bp import auth
    app.register_blueprint(index, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

