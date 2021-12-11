from flask import Blueprint, request, flash
from flask.templating import render_template
from flask_login import login_manager, login_user
from ..models.user import User
from .. import db


register = Blueprint('register', __name__)


@register.route('/register/', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if len(first_name) <= 1:
            flash(f'{first_name} is too short for First Name', category='danger')
        elif len(last_name) <= 1:
            flash(f'{last_name} is too short for Last Name', category='danger')
        elif len(email) <= 1:
            flash(f'{email} is too short for Email', category='danger')
        elif '@' not in email or '.com' not in email:
            flash('Invalid Email format', category='danger')
        elif len(password) < 8:
            flash(f'{password} is too short for Password, Minimum length 8 characters', category='danger')
        elif confirm_password != password:
            flash(f'{confirm_password} does not match Password', category='danger')
        else:
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                flash('Email is already in use by another account', category='danger')
            else:
                full_name = first_name + ' ' + last_name
                try:
                    user = User(full_name=full_name, email=email, password=password)
                    db.session.add(user)
                    db.session.commit()
                    flash('User registered successfully')
                except:
                    flash('Internal server error, try again')
            
    return render_template('register.html')
