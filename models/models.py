from wsgi import (
    db
)

class Persona(db.Model):
    __tablename__='Persona'

    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.Text)
    edad=db.Column(db.Integer)
    pais=db.Column(db.Text)

    def __init__(self, nombre, edad, pais):
        self.nombre=nombre
        self.edad=edad
        self.pais=pais
    
    def __repr__(self):
        return f'Persona: nombre {self.nombre}, edad {self.edad} y pais {self.pais}'

class Mascota(db.Model):
    __tablename__='Mascotas'

    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.Text)
    juguetes=db.relationship('juguete', backref='mascota', userList=False)
    propietario=db.relationship('propietario', backref='mascota', userList=False)

    def __init__(self, nombre):
        self.nombre=nombre

    def __repr__(self):
        return f'Mascota: {self.nombre}'

    def mostrar_juguetes(self):
        for juguete in self.juguetes:
            print(juguete.nombre)

class Juguete(db.Model):
    __tablename__='Juguetes'

    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.Text)
    mascota_id=db.Column(db.Integer, db.ForeignKey('Mascotas.id'))

    def __init__(self, nombre, mascota_id):
        self.nombre=nombre
        self.mascota_id=mascota_id

    def __repr__(self):
        return f'Mascota: {self.nombre}'

class Propietario(db.Model):
    __tablename__='Propietarios'

    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.Text)
    mascota_id=db.Column(db.Integer, db.ForeignKey('Mascotas.id'))

    def __init__(self, nombre, mascota_id):
        self.nombre=nombre
        self.mascota_id=mascota_id

    def __repr__(self):
        return f'Mascota: {self.nombre}'

         