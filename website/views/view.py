from flask import Blueprint, render_template


view = Blueprint('view', __name__)

@view.route('/features/')
def features():
    return '<h1>Features</h1>'

@view.route('/about/')
def about():
    return '<h1>Shediastis V1.0</h1></br><h1>Created by : <em>Kawshik Biswas</em></h1>'
