from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, NumberRange
from app.models import User

class SettingsForm(FlaskForm):
    type_of_break = StringField('What do you want to do on your break?', validators=[DataRequired()])
    time = IntegerField('How long you want to spend working?', validators=[DataRequired(), NumberRange(min=1, max=60)])
    break_time = IntegerField('How long you want to break for?', validators=[DataRequired(), NumberRange(min=5, max=10)])
    submit = SubmitField('Submit')
