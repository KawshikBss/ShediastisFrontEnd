from flask import Blueprint, redirect, url_for, request, render_template, flash, json, jsonify
from flask_login import current_user, login_required
from ..models.task import Task
from .. import db


dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard/', methods=['POST', 'GET'])
@login_required
def dashboard_page():
    if not current_user.is_authenticated or not current_user:
        flash('User is not authorized to use that page')
        return redirect(url_for('dashboard.dashboard_page'))
    current_tasks = current_user.get_current_tasks()
    completed_tasks = current_user.get_completed_tasks()
    trashed_tasks = current_user.get_trashed_tasks()
    return render_template('dashboard.html', user=current_user, current_tasks=current_tasks, completed_tasks=completed_tasks, trashed_tasks=trashed_tasks, time='9:00 AM')

@dashboard.route('/manage_task/', methods=['POST'])
@login_required
def manage_task():
    if not current_user.is_authenticated:
        flash('User is not authorized to use that action')
        return redirect(url_for('dashboard.dashboard_page'))
    task_id = json.loads(request.data)['taskId']
    task = Task.query.filter_by(id=task_id).first()
    if task:
        current_status = task.get_status()
        if current_status == 'Open':
            task.change_completed()
        elif current_status == 'Completed':
            task.change_trashed()
        else:
            task.delete_task()
        db.session.commit()
    return jsonify({})

@dashboard.route('/add_task/', methods=['POST'])
@login_required
def add_task():
    if not current_user.is_authenticated:
        flash('User is not authorized to use that action')
        return redirect(url_for('dashboard.dashboard_page'))
    new_task_desc = json.loads(request.data)['task']
    if len(new_task_desc) > 2:
        try:
            new_task = Task(current_user.id, new_task_desc)
            db.session.add(new_task)
            db.session.commit()
            flash('Task added')
        except:
            flash('Internal server error', category='danger')
    return jsonify({})
