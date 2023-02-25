from flask import (
    Flask
)
from routes import (
    routes
)
from flask_sqlalchemy import (
    SQLAlchemy
)
from flask_migrate import (
    Migrate
)
import os

directorio=os.path.abspath(os.path.dirname(__file__))
db_path=os.path.join(directorio,'datos.sqlite')
app=Flask(__name__)
app.config['SECRET_KEY']=os.getenv('SECRET_KEY', 'HOLA')
app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key=os.getenv('SECRET_KEY', 'HOLA')

#base de datos
db=SQLAlchemy(app)
Migrate(app, db)
#routes
routes(app=app, db=db)
