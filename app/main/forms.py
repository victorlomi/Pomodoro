from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class SettingsForm(FlaskForm):
    type_of_break = StringField('Type of break', validators=[DataRequired()])
    time = IntegerField('How long you want to spend working?', validators=[DataRequired()]) 
    submit = SubmitField('Submit')
