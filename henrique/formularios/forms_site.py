from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, EmailField, PasswordField, DateField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from wtforms import validators

from henrique.modelos import *


class Login_sis(FlaskForm):
    email = EmailField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 20)])
    btn_login = SubmitField('Logar')


class Novo_user(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    nova_senha = PasswordField('Nova Senha', validators=[DataRequired(), Length(8, 20)])
    confirme_senha = PasswordField('Confirmar Senha',
                                   validators=[DataRequired(), EqualTo('nova_senha', message='A senha não confere')])
    btn_criar = SubmitField('Criar Acesso')

    def validate_email(self, email):
        usuario = Usuarios.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já está cadastrado em nossa plataforma')

