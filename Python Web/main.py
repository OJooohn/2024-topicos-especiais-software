from flask import Flask, render_template, redirect

from formulario import FormularioCriarConta

app = Flask(__name__)

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def menu():
    # return "<h1>Hello, World!</h1>"
    formularioConta = FormularioCriarConta()
    return render_template('menu.html', form=formularioConta)

@app.route('/perfil/<id_usuario>')
def perfil(id_usuario):
    return render_template('perfil.html', usuario=id_usuario)

# flask_wtf

if __name__ == '__main__':
    app.run(debug = True)

