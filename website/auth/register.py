from flask import Blueprint, request, flash
from flask.templating import render_template
from ..models.user import User
from ..others.validation import validate_name_len, validate_email, validate_password
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
        
        if validate_name_len(first_name):
            flash(f'{first_name} is too short for First Name', category='danger')
        elif validate_name_len(last_name):
            flash(f'{last_name} is too short for Last Name', category='danger')
        elif validate_name_len(email):
            flash(f'{email} is too short for Email', category='danger')
        elif validate_email(email):
            flash('Invalid Email format', category='danger')
        elif validate_password(password):
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
                    db.session.add(User(fullname=full_name, email=email, password=password))
                    db.session.commit()
                    flash('User registered successfully')
                except:
                    flash('Internal server error, try again', category='danger')
            
    return render_template('register.html')
