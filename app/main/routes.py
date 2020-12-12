from flask import render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.models import User
from app.main import bp
from app.main.forms import SettingsForm
from app import db

@bp.route('/')
def index():
    return render_template('index.html') 

@bp.route('/settings', methods=["GET", "POST"])
def settings():
    if current_user.is_anonymous:
        return redirect(url_for("auth.login"))

    form = SettingsForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            user = User.query.filter_by(username=current_user.username).first()
            user.type_of_break = form.type_of_break.data
            user.time = form.time.data
            user.break_time = form.break_time.data
            db.session.commit()

        return redirect(url_for('main.timer'))

    return render_template('settings.html', form=form)


@bp.route('/timer')
def timer(): 
    return  render_template('timer.html', user=current_user)
