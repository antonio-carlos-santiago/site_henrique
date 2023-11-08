from henrique import db, login_manager
from flask_login import UserMixin
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


@login_manager.user_loader
def load_user(id_usuario):
    return Usuarios.query.get(int(id_usuario))


class Usuarios(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String, nullable=False)
    adminstrador: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False)


class Vendedores(db.Model):
    id_vendedor: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    cpf_cnpj: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    data_cadastro: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    comissionamento: Mapped[str] = mapped_column(String, nullable=False)



class Clientes(db.Model):
    id_cliente: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    cpf: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    data_nascimento: Mapped[str] = mapped_column(DateTime, unique=False, nullable=False)
    rg: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    telefone: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    cep: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    estado: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    cidade: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    endereco: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    numero_residencia: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, unique=False, nullable=False, default=False)
    data_adesao: Mapped[str] = mapped_column(DateTime, unique=False, nullable=False, default=datetime.utcnow)
    data_fim_contrato: Mapped[str] = mapped_column(DateTime, nullable=True)
    id_vendedor: Mapped[int] = mapped_column(Integer, ForeignKey("vendedores.id_vendedor"))
    vendedores = db.relationship("Vendedores", backref="clientes")



class Listaparticipantes(db.Model):
    id_participante: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    cpf: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    id_cliente: Mapped[int] = mapped_column(Integer, ForeignKey('clientes.id_cliente'))
    cliente_responsavel = db.relationship("Clientes", backref="listaparticipantes")



class Empresassocias(db.Model):
    id_empresa: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    cnpj: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    cep: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    estado: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    cidade: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    endereco: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    numero_residencia: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, unique=False, default=True)
    data_cadastro: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    data_fim_contrato: Mapped[str] = mapped_column(DateTime, nullable=False)



class Servicosdisponiveis(db.Model):
    id_servico: Mapped[int] = mapped_column(Integer,primary_key=True)
    nome_servico: Mapped[str] = mapped_column(String, nullable=False)
    desconto: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    user_cadastro: Mapped[str] = mapped_column(String, nullable=False)
    data_cadastro: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    id_empresas: Mapped[int] = mapped_column(Integer, ForeignKey("empresassocias.id_empresa"))
    empresa = db.relationship("Empresassocias", backref="servicosdisponiveis")
