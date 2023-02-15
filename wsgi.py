from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
)

app = Flask(__name__)

@app.route("/")
def home():
    return "<h6>Home</h6>"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f'<h1> Hola {nombre}</h1>'

@app.route("/edad/<int:edad>")
def get_edad(edad):
    return f'<h3> Tu edad es: {edad}</h3>'

@app.route("/mostrar/<nombre>",methods=['GET', 'POST'])
def get_mostrar(nombre):
    return render_template('mostrar.html', nombre_parametro=nombre)

@app.route("/redirect")
def get_redirect():
    return redirect(url_for('home'))