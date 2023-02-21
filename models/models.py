from wsgi import (
    db
)

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
         