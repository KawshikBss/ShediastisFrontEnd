from flask import Blueprint


register = Blueprint('register', __name__)


@register.route('/register/', methods=['GET', 'POST'])
def registration():
    return '<h1>REg</h1>'
