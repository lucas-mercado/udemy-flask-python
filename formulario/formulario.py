from flask_wtf import (
    FlaskForm
)
from wtforms import (
    StringField,
    SubmitField
)
class Formulario(FlaskForm):
    nombre=StringField('nombre')
    estado=SubmitField('estado')
