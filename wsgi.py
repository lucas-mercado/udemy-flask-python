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

@app.errorhandler(404)
def error_handler(error):
    return render_template('404.html', error=error)

@app.route('/signin/<usuario>/<password>')
def sign_in(usuario, password):
    db_user='Lucas'
    db_pass='123456'
    if usuario==db_user and password==db_pass:
        return f'Exitoso User: {usuario}'
    return render_template('404.html',error=f'Fallo User -> {usuario}')

@app.route('/personas')
def get_personas():
    personas=['lucas', 'debora', 'agustin']
    return render_template('mostrar_personas.html', personas=personas)

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')