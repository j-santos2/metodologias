import logging
from os import getenv

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,
    static_url_path='', 
    static_folder='static')
db = SQLAlchemy()


def create_app():
    app.logger.setLevel(logging.INFO)

    # DB CONFIG
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if getenv('ENVIRONMENT', 'DEV'):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../test.db'
    else:
        db_host = getenv('DB_HOST')
        app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:pass@{db_host}:5432/app_dev'

    # VIEWS
    from happy_paws.blueprints.index_bp import index
    from happy_paws.blueprints.auth_bp import auth
    app.register_blueprint(index, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # DB INIT
    from .models import User

    create_database(app)

    # LOGIN SESSION INIT
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app=app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
