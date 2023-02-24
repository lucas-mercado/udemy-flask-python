from wsgi import (
    db,
    app
)
from models.models import(
    Mascota,
    Propietario,
    Juguete
)

app.app_context().push()

''' Creamos las mascotas'''
mascota1=Mascota('Felipe')
mascota2=Mascota('Cati')
db.session.add_all([mascota1, mascota2])
db.session.commit()

'''Todas las mascotas'''
mascotas=Mascota.query.all()
print(f'mascotas : {mascotas}')

'''busco una mascota por nombre'''
mascota_felipe=Mascota.query.filter_by(nombre='Felipe').first()

''' Creo Propietario'''
propietario1=Propietario('Pedro', mascota_felipe.id)
db.session.add(propietario1)
db.session.commit()

''' Creo juguete'''
juguete1=Juguete('Pelota de Futbol', mascota_felipe.id)
juguete2=Juguete('Oso de Peluche', mascota_felipe.id)
db.session.add_all([juguete1, juguete2])
db.session.commit()


