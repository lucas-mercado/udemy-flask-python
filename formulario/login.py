from flask_wtf import (
    FlaskForm
)
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
)
class Login(FlaskForm):
    username=StringField('username')
    password=PasswordField('password')
    boton=SubmitField('enviar')

class LogOut(FlaskForm):
    logout=SubmitField('logout')