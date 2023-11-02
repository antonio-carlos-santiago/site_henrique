from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, EmailField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from henrique.modelos import Usuarios


class Login_sis(FlaskForm):
    email = EmailField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 20)])
    btn_login = SubmitField('Logar')


class Novo_user(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    nova_senha = PasswordField('Nova Senha', validators=[DataRequired(), Length(6, 15)])
    confirme_senha = PasswordField('Confirmar Senha',
                                   validators=[DataRequired(), EqualTo('nova_senha', message='A senha não confere')])
    btn_criar = SubmitField('Criar Acesso')

    def validate_email(self, email):
        usuario = Usuarios.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já está cadastrado em nossa plataforma')


class Novo_contracheque(FlaskForm):
    servidor = SelectField('Tipo Servidor', choices=[('31', 'Pensionista'), ('01', 'Ativos'), ('01', 'Aposentado')],
                           validators=[DataRequired()])
    cpf = StringField('Informe o CPF', validators=[DataRequired(), Length(11, 11)])
    matricula = StringField('Informe a Matricula', validators=[DataRequired(), Length(8)])
    mes = SelectField('Informe o Mês',
                      choices=[('01'), ('02'), ('03'), ('04'), ('05'), ('06'), ('07'), ('08'), ('09'), ('10'), ('11'),
                               ('12')], validators=[DataRequired()])
    ano = SelectField('Informe o Ano', choices=[('2021'), ('2022')], validators=[DataRequired()])
    btn_gerar = SubmitField('Gerar Contracheque')


class Consulta_Prodan(FlaskForm):
    cpf = StringField('Informe o CPF', validators=[DataRequired(), Length(11, 11)])
    btn_consultar = SubmitField('Consultar')


class Consulta_Consiglog(FlaskForm):
    matricula = StringField('Informe a Matricula', validators=[DataRequired(), Length(8, 8)])
    btn_consultar = SubmitField('Consultar')
