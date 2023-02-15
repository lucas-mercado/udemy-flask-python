from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f'<h1> Hola {nombre}</h1>'

@app.route("/edad/<int:edad>")
def get_edad(edad):
    return f'<h3> Tu edad es: {edad}</h3>'