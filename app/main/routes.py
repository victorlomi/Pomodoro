from flask import render_template, redirect, url_for
from app.main import bp
from app.main.forms import SettingsForm

@bp.route('/')
def index():
    return render_template('index.html') 

@bp.route('/settings', methods=["GET", "POST"])
def settings():
    form = SettingsForm()
    if form.validate_on_submit():
        return redirect(url_for('main.timer')) 
    return render_template('settings.html', form=form)


@bp.route('/timer')
def timer():
    return 'timer'