from flask import Flask, Blueprint
from flask_login import login_manager
from os import path
from flask_sqlalchemy import SQLAlchemy


DB_NAME = 'database.db'
db = SQLAlchemy()


def create_app(config_filename):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_filename)

    db.init_app(app=app)
    #create_db(app=app)

    from .views.index import index
    from .views.view import view
    from .auth.register import register


    app.register_blueprint(index, url_prefix='/')
    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(register, url_prefix='/')

    return app


def create_db(app):
    if not path.exists(DB_NAME):
        db.create_all(app=app)
