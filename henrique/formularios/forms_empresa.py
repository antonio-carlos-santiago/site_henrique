
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from henrique.funcoes.funcoes_status_alteracao import *
from henrique.modelos import *



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
            raise ValidationError("Essa empresa já possui cadastro")



class BuscarEmpresa(FlaskForm):
    cnpj = StringField("CNPJ", validators=[DataRequired(message="Campo Obrigatório"), Length(14, 14)])
    btn_busca = SubmitField("Buscar Master")

    def validate_cnpj(self, cnpj):
        buscar_empresa = Empresassocias.query.filter_by(cnpj=cnpj.data).first()
        if not buscar_empresa:
            raise ValidationError("Empresa não encontrada")
        

class RegistrarServico(FlaskForm):
    lista_descontos = [(f"{desconto}", f"{desconto} %") for desconto in range(10, 91)]


    cnpj = StringField("CNPJ")
    servico = StringField("Informe o Serviço", validators=[DataRequired("Campo Obrigatorio")])
    desconto = SelectField("Informe o Desconto",choices=lista_descontos, validators=[DataRequired("Campo Obrigatorio")])
    btn_reg_serv = SubmitField("Registar")


    def validate_servico(self, servico):
        servicodisponivel = Servicosdisponiveis.query.all()
        for servicos in servicodisponivel:
              if servicos.nome_servico == servico.data.upper() and servicos.empresa.cnpj == self.cnpj.data:
                    raise ValidationError("Este serviço já consta cadastrado para essa empresa")



class BuscarEmpresas(FlaskForm):
    def empresas_validadas():
        return ListarEmpresas()
    
    empresas = SelectField("Empresa", choices=empresas_validadas, validators=[DataRequired()])
    btn_conf = SubmitField('Buscar Cadastro')



class AtualizacaoEmpresa(FlaskForm):
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

    statusemp = [
        ('', "Indefinido"),
        ("1", "Ativa"),
        ("0", 'Inativa')
    ]


    nome = StringField("Nome Fantasia")
    nome_origem = HiddenField()
    cep = StringField("Cep", validators=[DataRequired(message="Campo Obrigatório"), Length(8, 8)])
    estado = SelectField("Estado", choices=estados, validators=[DataRequired(message="Campo Obrigatório")])
    cidade = SelectField("Cidade", choices=cidades, validators=[DataRequired(message="Campo Obrigatório")])
    endereco = StringField("Endereço", validators=[DataRequired(message="Campo Obrigatório")])
    numero_residencia = StringField("Numero", validators=[DataRequired(message="Campo Obrigatório")])
    status = SelectField("Status", choices=statusemp, validators=[DataRequired()])
    telefone = StringField("Telefone", validators=[DataRequired()])
    btn_atualizar_empresa = SubmitField("Atualizar")



class BuscarServicos(FlaskForm):
    servicos = SelectField("Servicos", choices=[("", "BUSQUE A EMPRESA ANTES")])
    empresa = HiddenField()
    btn_conf_servico = SubmitField('Verificar Serviço')




class AtualizacaoServicos(FlaskForm):
    statusserv = [
        ('', "Indefinido"),
        ("1", "Ativa"),
        ("0", 'Inativa')
    ]

    lista_descontos = [(f"{desconto}", f"{desconto} %") for desconto in range(1, 95)]


    nome_empresa = StringField("Prestadora de serviço", validators=[DataRequired()])
    cnpj_empresa = StringField("CNPJ Responsavel", validators=[DataRequired()])
    nome_servico = StringField("Serviço ofertado", validators=[DataRequired()])
    desconto = SelectField("Desconto por indicação", choices=lista_descontos, validators=[DataRequired()])
    status_servico = SelectField("Status de serviço", choices=statusserv, validators={DataRequired()})
    btn_atualiza_servico = SubmitField("Atualizar Dados")


    