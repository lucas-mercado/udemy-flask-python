from flask import (
    Flask
)
from routes import (
    routes
)
from flask_sqlalchemy import (
    SQLAlchemy
)
import os

directorio=os.path.abspath(os.path.dirname(__file__))
db_path=os.path.join(directorio,'datos.sqlite')
app=Flask(__name__)
app.config['SECRET_KEY']=os.getenv('SECRET_KEY', 'HOLA')
app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#base de datos
db=SQLAlchemy(app)

#models 
class Persona(db.Model):
    __tablename__='Persona'

    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.Text)
    edad=db.Column(db.Integer)

    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    
    def __repr__(self):
        return f'Persona: nombre {self.nombre} y edad {self.edad}'

#routes
routes(app=app)
