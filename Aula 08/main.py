# pip install -r requirements.txt

from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from config import app
from forms import RegisterForm, EventForm
from models import *

@app.route('/')
def home():
    return render_template('index.html')
#:D awo

@app.route('/register', methods=['GET', 'POST'])
def register():
    from forms import RegisterForm
    from werkzeug.security import generate_password_hash

    formulario = RegisterForm()

    if formulario.validate_on_submit():
        usu = formulario.username.data

        sen = generate_password_hash(formulario.password.data)
        print(f'-- {usu} -- {sen}')

        usu_ex = User.query.filter_by(username=usu).first()
        if usu_ex:
            print('Usuario ja existe')
        else:
            novo_usuario = User(username=usu, password=sen)
            db.session.add(novo_usuario)
            db.session.commit()
            print('Usuario Criado')
            # redirecionar
            return redirect(url_for('login'))

    return render_template('register.html', form=formulario)


@app.route('/login', methods=['GET', 'POST'])
def login():
    from forms import LoginForm
    from werkzeug.security import check_password_hash

    formulario = LoginForm()

    if formulario.validate_on_submit():
        usuStr = formulario.username.data

        usuBanco = User.query.filter_by(username=usuStr).first()
        if usuBanco:
            senhaDigitada = formulario.password.data
            senhaBanco = usuBanco.password

            if check_password_hash(senhaBanco, senhaDigitada):
                login_user(usuBanco)
                print('penis')
                return redirect(url_for('dashboard'))
            # else:
                # erro


    return render_template('login.html', form=formulario)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    from forms import EventForm

    formulario = EventForm()

    if formulario.validate_on_submit():
        nomeEvento = formulario.event_name.data
        dataEvento = formulario.event_date.data
        descEvento = formulario.description.data



        usuBanco = User.query.filter_by(id=current_user.id).first()

        eventoBanco = Event.query.filter_by(event_name=nomeEvento).first()

        print(f'-- {nomeEvento} -- {dataEvento} -- {descEvento}')

        if eventoBanco:
            print('Evento ja existente')
        else:
            novo_evento = Event(event_name=nomeEvento, event_date=dataEvento, description=descEvento, user_id=usuBanco.id)
            db.session.add(novo_evento)
            db.session.commit()
            print('Evento Criado')
            # redirecionar
            return redirect(url_for('dashboard'))


    return render_template('create_event.html', form=formulario)


@app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    return render_template('edit_event.html')


@app.route('/delete_event/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
