from flask import Blueprint


index = Blueprint('index', __name__)


@index.route('/')
@index.route('/index/')
def index_page():
    return '<h1>Hello World</h1>'
