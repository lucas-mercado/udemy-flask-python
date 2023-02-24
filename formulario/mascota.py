from flask_wtf import (
    FlaskForm
)
from wtforms import (
    StringField,
    SubmitField,
    IntegerField
)

class FormularioAlta(FlaskForm):
    nombre=StringField('ingrese nombre mascota')
    boton=SubmitField('agregar')

class FormularioBaja(FlaskForm):
    id=IntegerField('Ingrese id de la mascota')
    boton=SubmitField('Delete Mascota')