from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class SettingsForm(FlaskForm):
    type_of_break = StringField('What do you want to do on your break?', validators=[DataRequired()])
    time = IntegerField('How long you want to spend working?', validators=[DataRequired()])
    break_time = IntegerField('How long you want to break for?', validators=[DataRequired()])
    submit = SubmitField('Submit')
