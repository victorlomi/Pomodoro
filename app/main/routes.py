from flask import render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from hashlib import md5
from app.models import User
from app.main import bp
from app.main.forms import SettingsForm
from app import db

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/profile')
def profile():
    return render_template('profile.html', user=current_user) 

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

        return redirect(url_for('main.timer', type_of_timer="work"))

    return render_template('settings.html', form=form)


@bp.route('/timer/<type_of_timer>')
def timer(type_of_timer):
    if type_of_timer == "work":
        return  render_template('work_timer.html', user=current_user)
    else:
        return  render_template('break_timer.html', user=current_user)
