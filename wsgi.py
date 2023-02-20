from flask import (
    Flask
)
from routes import (
    routes
)
import os

app = Flask(__name__)
app.config['SECRET_KEY']=os.getenv('SECRET_KEY', 'HOLA')
routes(app=app)
