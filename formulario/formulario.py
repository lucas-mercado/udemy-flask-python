from flask_wtf import (
    FlaskForm
)
from wtforms import (
    StringField,
    SubmitField,
    BooleanField,
    TextAreaField,
    RadioField
)
from wtforms.validators import (
    DataRequired
)
class Formulario(FlaskForm):
    nombre=StringField('nombre', validators=[DataRequired()])
    edad=BooleanField('Eres mayor de edad')
    sexo=RadioField('sexo: ', choices=[('H', 'Hombre'),('M', 'Mujer')])
    comentario=TextAreaField()
    boton=SubmitField('Enviar')
