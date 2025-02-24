from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import  DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),Length(min=2, max=100)])
    email = StringField('e-mail',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=8, max=32), DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[Length(min=8, max=32), DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('e-mail',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=8, max=32), DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
