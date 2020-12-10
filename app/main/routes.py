from flask import render_template
from app.main import bp
from app.main.forms import SettingsForm

@bp.route('/')
def index():
    return render_template('index.html') 

@bp.route('/settings')
def settings():
    form = SettingsForm()
    return render_template('settings.html', form = form)