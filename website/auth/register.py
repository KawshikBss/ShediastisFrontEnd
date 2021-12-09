from flask import Blueprint, request
from flask.templating import render_template


register = Blueprint('register', __name__)


@register.route('/register/', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        print(first_name + last_name + email + password + confirm_password)
    return render_template('register.html')
