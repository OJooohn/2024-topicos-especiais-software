from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class FormularioCriarConta(FlaskForm):
    nome = StringField('Nome:', validators=[DataRequired()])
    email = EmailField('Email:', validators=[DataRequired(), Email()])

    senha = PasswordField('Senha:', validators=[DataRequired()])
    confirmarSenha = StringField('Confirmar senha:', validators=[DataRequired(), EqualTo(senha)])

    btn = SubmitField('Criar Conta')


