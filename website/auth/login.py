from flask import Blueprint, request, render_template, url_for, flash
from flask_login import login_manager, login_user
from flask_login.utils import login_required, logout_user
from werkzeug.utils import redirect
from ..models.user import User
from werkzeug.security import check_password_hash
from ..others.validation import validate_name_len, validate_email, validate_password


login = Blueprint('login', __name__)

@login.route('/login/', methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if validate_name_len(email):
            flash('Email is too short', category='danger')
        elif validate_email(email):
            flash('Incorrect email format', category='danger')
        elif validate_password(password):
            flash('Password is too short', category='danger')
        else:
            user = User.query.filter_by(email=email).first()
            if not user:
                flash('No such user found', category='danger')
            else:
                if check_password_hash(user.password, password):
                    login_user(user=user, remember=True)
                    flash('Login successfull')
                    return redirect(url_for('dashboard.dashboard_page'))
                else:
                    flash('Incorrect password', category='danger')

    return render_template('login.html')

@login.route('/logout/')
def logout():
    logout_user()
    flash('User logged out')
    return redirect(url_for('login.login_page'))
