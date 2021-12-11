from flask import Blueprint, request, render_template, flash
from flask_login import current_user, login_required


dashboard = Blueprint('dashboard', __name__)

@login_required
@dashboard.route('/dashboard/', methods=['POST', 'GET'])
def dashboard_page():

    return render_template('dashboard.html', user=current_user)
