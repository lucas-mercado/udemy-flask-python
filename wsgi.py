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

#routes
routes(app=app)
