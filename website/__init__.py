from flask import Flask, Blueprint
from flask_login import LoginManager, login_manager
from os import path
from flask_sqlalchemy import SQLAlchemy


DB_NAME = 'database.db'
db = SQLAlchemy()


def create_app(config_filename):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_filename)

    db.init_app(app=app)
    create_db(app=app)

    from .views.index import index
    from .views.view import view
    from .views.dashboard import dashboard
    from .auth.register import register
    from .auth.login import login


    app.register_blueprint(index, url_prefix='/')
    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(register, url_prefix='/')
    app.register_blueprint(login, url_prefix='/')
    app.register_blueprint(dashboard, url_prefix='/')

    loginManager = LoginManager()
    loginManager.login_view = 'login.login_page'
    loginManager.init_app(app=app)

    from .models.user import User

    @loginManager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_db(app):
    if not path.exists(DB_NAME):
        from .models.user import User
        from .models.task import Task
        db.create_all(app=app)
