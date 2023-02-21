'''
Deprecated since version 2.0: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. 
The method is now available as Session.get() (Background on SQLAlchemy 2.0 at: SQLAlchemy 2.0 - Major Migration Guide)
https://docs.sqlalchemy.org/en/20/changelog/migration_20.html#migration-20-query-usage
example:
    session.query(User).get(42) ---------> session.get(User, 42)
'''

from wsgi import (
    app,
    db,
)
from models.models import (
    Persona
)

app.app_context().push()
db.create_all()

persona1=Persona('Pedro', 25)
persona2=Persona('Maria', 35)
db.session.add_all([persona1, persona2])
db.session.commit()

persona3=Persona('Teresa', 24)
db.session.add(persona3)
db.session.commit()

personas=Persona.query.all()

print(f'Veremos todas las personas: \n {personas}')

filtro1=Persona.query.filter_by(nombre='Pedro')
print(f'buscamos a un nombre por filtro \n {filtro1.all()}')

# select_id=db.session.query(Persona).get(1) deprecated
select_id=db.session.get(Persona, 1)
print(f'Persona por id: \n {select_id}')

#update persona
#persona_update=db.session.query(Persona).get(3) deprecada
#persona_update=Persona.query.get(3) deprecada
persona_update=db.session.get(Persona, 3)

persona_update.edad=34
db.session.add(persona_update)
db.session.commit()
print(f'Acaba de actualiza a la persona: \n {persona_update}')

#delete persona
try:
    # persona_borrar=db.session.query(Persona).get(2) deprecated
    persona_borrar=db.session.get(Persona, 2)
    db.session.delete(persona_borrar)
    db.session.commit()
    print(f'Acaba de borrar a la persona: \n {persona_borrar}')
except Exception as e:
    print('no existe persona con id 2')

personas=Persona.query.all()
print(f'Registro de personas final \n {personas}')


