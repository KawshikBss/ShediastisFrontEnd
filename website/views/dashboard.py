from flask import Blueprint, request, render_template, flash, json, jsonify
from flask_login import current_user, login_required


dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard/', methods=['POST', 'GET'])
@login_required
def dashboard_page():

    return render_template('dashboard.html', user=current_user, time='9:00 AM')

@dashboard.route('/manage_task/', methods=['POST'])
@login_required
def manage_task():
    task_id = json.loads(request.data)['taskId']
    print(task_id)
    return jsonify({})
