from flask import render_template
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html') 

@bp.route('/settings')
def settings():
    return render_template('settings.html')