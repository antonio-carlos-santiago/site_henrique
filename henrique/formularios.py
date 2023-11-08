from flask_wtf import FlaskForm
from numpy import diag
from wtforms import SubmitField, StringField, EmailField, PasswordField, DateField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from wtforms import validators

from henrique.modelos import Usuarios, Empresassocias


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



class NovaEmpresa(FlaskForm):

    estados = [
        ('', 'Escolha um estado'),
        ('AM', 'Amazonas'),        
    ]

    cidades = [
        ('', 'Escolha uma cidade'),
        ('Manaus', 'Manaus')
    ]

    tempo_adesao = [
        ('', 'Escolha o tempo de adesão'),
        ("1",'1 ano'),
        ("2",'2 anos'),
        ("3",'3 anos'),
        ("4",'4 anos'),
        ("5",'5 anos'),
    ]


    nome = StringField("Nome Fantasia", validators=[DataRequired(message="Campo Obrigatório")])
    cnpj = StringField("CNPJ", validators=[DataRequired(message="Campo Obrigatório"), Length(14, 14)])
    cep = StringField("Cep", validators=[DataRequired(message="Campo Obrigatório"), Length(8, 8)])
    estado = SelectField("Estado", choices=estados, validators=[DataRequired(message="Campo Obrigatório")])
    cidade = SelectField("Cidade", choices=cidades, validators=[DataRequired(message="Campo Obrigatório")])
    endereco = StringField("Endereço", validators=[DataRequired(message="Campo Obrigatório")])
    numero_residencia = StringField("Numero", validators=[DataRequired(message="Campo Obrigatório")])
    adesao = SelectField("Tempo de Adesão", choices=tempo_adesao, validators=[DataRequired(message="Campo Obrigatório")])
    btn_cadastrar_empresa = SubmitField("Cadastrar Empresa")

    def validate_cnpj(self, cnpj):
        empresas = Empresassocias.query.filter_by(cnpj=cnpj.data).first()
        if empresas:
            raise ValidationError("CNPJ já cadastrado !!!")




class NovoCliente(FlaskForm):
    estados = [
        ('', 'Escolha um estado'),
        ('AM', 'Amazonas'),        
    ]

    cidades = [
        ('', 'Escolha uma cidade'),
        ('Manaus', 'Manaus')
    ]

    tempo_adesao = [
        ('', 'Escolha o tempo de adesão'),
        ("1",'1 ano'),
        ("2",'2 anos'),
        ("3",'3 anos'),
        ("4",'4 anos'),
        ("5",'5 anos'),
    ]

    nome = StringField("Nome", validators=[DataRequired()])
    cpf = StringField("CPF", validators=[DataRequired(), Length(11)])
    data_nascimento = DateField("Data de Nascimento", format='%d/%m/%Y', validators=[DataRequired(message="Campo Obrigatório")])
    rg = StringField("RG", validators=[DataRequired(message="Campo Obrigatório")])
    telefone = StringField("Telefone", validators=[DataRequired(message="Campo Obrigatório")])
    email = EmailField("Email", validators=[DataRequired(message="Campo Obrigatório"), Email()])
    cep = StringField("CEP", validators=[DataRequired(message="Campo Obrigatório"), validators.Regexp(r'^\d{5}-\d{3}$', message="Formato de CEP inválido. Use o formato 12345-678.")])
    estado = SelectField("Estado", choices=estados, validators=[DataRequired(message="Campo Obrigatório")])
    cidade = SelectField("Cidade", choices=cidades, validators=[DataRequired(message="Campo Obrigatório")])
    endereco = StringField("Endereço", validators=[DataRequired(message="Campo Obrigatório")])
    numero_residencia = StringField("Numero Residencia", validators=[DataRequired(message="Campo Obrigatório")])
    adesao = SelectField("Tempo de Adesão", choices=tempo_adesao, validators=[DataRequired(message="Campo Obrigatório")])
    btn_cadastrar_cliente = SubmitField("Cadastrar Cliente")



class BuscarCliente(FlaskForm):
    cpf_cliente = StringField("CPF Conta Master", validators=[DataRequired(message="Campo Obrigatório"), Length(11, 11)])
    btn_busca = SubmitField("Buscar Master")



class BuscarEmpresa(FlaskForm):
    cnpj = StringField("CNPJ", validators=[DataRequired(message="Campo Obrigatório"), Length(14, 14)])
    btn_busca = SubmitField("Buscar Master")

    def validate_cnpj(self, cnpj):
        buscar_empresa = Empresassocias.query.filter_by(cnpj=cnpj.data).first()
        if not buscar_empresa:
            raise ValidationError("Empresa não encontrada")
        


class CadastrarParticipante(FlaskForm):
    nome_participante = StringField("Nome Participante", validators=[DataRequired(message="Campo Obrigatório")])
    cpf_participante = StringField("CPF Participante", validators=[DataRequired(message="Campo Obrigatório"), Length(11, 11)])
    btn_cadastrar_participante = SubmitField("Cadastrar Participante")
