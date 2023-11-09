from henrique.modelos import *
from henrique import db, app



def BuscaServicosDb(empresa):

    todos_servicos = Servicosdisponiveis.query.all()
    lista_servico = [(servicos.nome_servico, servicos.nome_servico) for servicos in todos_servicos if servicos.empresa.nome == empresa  ]
    return lista_servico



def ListarEmpresas():
    cadastros_empresas = Empresassocias.query.all()
    lista_empresas = [empresa.nome for empresa in cadastros_empresas]
    return lista_empresas
    


def PesquisaPorEmpresa(empresa):
    empresaprocurada = Empresassocias.query.filter_by(nome=empresa).first()
    
    dados = {}
    dados['nome'] = empresaprocurada.nome
    dados['cep'] = empresaprocurada.cep
    dados['estado'] = empresaprocurada.estado
    dados['cidade'] = empresaprocurada.cidade
    dados['endereco'] = empresaprocurada.endereco
    dados['numero_residencia'] = empresaprocurada.numero_residencia
    dados['telefone'] = empresaprocurada.telefone
    dados['data_cadastro'] = empresaprocurada.data_cadastro
    if empresaprocurada.status:
        dados['status'] = '1'
    else:
        dados['status'] = '0'

    return dados


def AtualizarDadosCadastrais(novosdados):
    print(novosdados.nome_origem.data)
    cadastro_atualizado = Empresassocias.query.filter_by(nome=novosdados.nome_origem.data).first()
    cadastro_atualizado.cep = novosdados.cep.data
    cadastro_atualizado.estado = novosdados.estado.data
    cadastro_atualizado.cidade = novosdados.cidade.data
    cadastro_atualizado.endereco = novosdados.endereco.data.upper()
    cadastro_atualizado.numero_residencia = novosdados.numero_residencia.data
    cadastro_atualizado.telefone = novosdados.telefone.data
    if int(novosdados.status.data):
        cadastro_atualizado.status = True
    else:
        cadastro_atualizado.status = False
    db.session.commit()


    for itens in novosdados:
        itens.data = ''
    return {"message": "Empresa Atualizada com sucesso", "status_notificacao": "alert-info"}


def PesquisaPorEmpresaComServico(empresa, servico):
    todos_servicos = Servicosdisponiveis.query.filter_by(nome_servico=servico).all()
    dados = {}
    for servicos_db in todos_servicos:
        if servicos_db.empresa.nome == empresa:
            dados['nome_servico'] = servicos_db.nome_servico
            dados['desconto'] = str(servicos_db.desconto)
            dados['nome'] = servicos_db.empresa.nome
            dados['cnpj'] = servicos_db.empresa.cnpj
            if servicos_db.status:
                dados['status'] = '1'
            else:
                dados['status'] = '0'

            return dados
                       




    """"s = Empresassocias.query.filter_by(nome=empresa).first()
    
    dados = {}
    dados['nome'] = empresaprocurada.nome
    dados['cep'] = empresaprocurada.cep
    dados['estado'] = empresaprocurada.estado
    dados['cidade'] = empresaprocurada.cidade
    dados['endereco'] = empresaprocurada.endereco
    dados['numero_residencia'] = empresaprocurada.numero_residencia
    dados['telefone'] = empresaprocurada.telefone
    dados['data_cadastro'] = empresaprocurada.data_cadastro
    if empresaprocurada.status:
        dados['status'] = '1'
    else:
        dados['status'] = '0'

    return dados"""
