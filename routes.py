def routes(app):
    from flask import (
        render_template,
        redirect,
        url_for,
        request,
        session,
        flash
    )
    
    @app.route("/")
    def home():
        return render_template('bienvenido.html')

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

    @app.route('/formulario')
    def formulario():
        return render_template('formulario.html')

    @app.route('/bienvenido')
    def bienvenido():
        return render_template('bienvenido.html',datos=request.args.to_dict())

    @app.route('/inicio', methods=['GET', 'POST'])
    def inicio():
        from formulario.formulario import (
            Formulario
        )
        
        datos = {
            "nombre" : '',
            "boton" : False,
            "formulario" : Formulario()
        }

        if datos['formulario'].validate_on_submit():
            datos['nombre'] = datos['formulario'].nombre.data
            datos['boton'] = True
            datos['formulario'].nombre.data = ''
        return render_template('inicio.html', datos=datos)


    @app.route('/informacion')
    def informacion():
        return render_template('informacion.html')

    @app.route('/datospersonales', methods=['GET', 'POST'])
    def datos_personales():
        from formulario.formulario import (
            Formulario
        )
        
        mi_formulario=Formulario()

        if mi_formulario.validate_on_submit():
            session['nombre']=mi_formulario.nombre.data
            session['edad']=mi_formulario.edad.data
            session['sexo']=mi_formulario.sexo.data
            session['comentario']=mi_formulario.comentario.data
            session['boton']=mi_formulario.boton.data
            return redirect(url_for('informacion'))
        return render_template('datospersonales.html',formulario=mi_formulario)

    @app.route('/generadormensaje/', methods=['GET', 'POST'])
    def generador_mensaje():
        from formulario.formulario import (
            FormularioBoton
        )
        mi_formulario=FormularioBoton()
        if mi_formulario.validate_on_submit():
            mensaje=mi_formulario.mensaje.data
            flash(mensaje)
            return redirect(url_for('generador_mensaje'))
        return render_template('alert.html',formulario=mi_formulario)