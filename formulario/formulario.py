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

class FormularioBoton(FlaskForm):
    '''
        Form:
            mensaje: String
            boton: Submit
    '''
    mensaje=StringField('mensaje')
    boton=SubmitField('Generar mensaje')

class Formulario(FlaskForm):
    '''
        Form:
            nombre: String
            edad: Bool
            sexo: Radio
            comentario: String
            boton: Submit
    '''
    nombre=StringField('nombre', validators=[DataRequired()])
    edad=BooleanField('Eres mayor de edad')
    sexo=RadioField('sexo: ', choices=[('H', 'Hombre'),('M', 'Mujer')])
    comentario=TextAreaField()
    boton=SubmitField('Enviar')
