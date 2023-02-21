from wsgi import (
    app,
    db,
)
from models.models import (
    Persona
)

app.app_context().push()

persona=db.session.get(Persona, 1)
persona.pais='Mexico'
db.session.add(persona)
db.session.commit()