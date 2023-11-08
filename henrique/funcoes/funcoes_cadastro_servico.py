from henrique.modelos import *
from henrique import db



def BuscarEmpresaDb(cnpj):
    empresa = Empresassocias.query.filter_by(cnpj=cnpj).first()
    if empresa:
        dados = {}
        if empresa.status:
            dados["status"] = "ATIVA"
        else:
            dados["status"] = "DESATIVADA"
        dados["cnpj"] = empresa.nome
        dados["nome"] = empresa.nome
        dados["cep"] = empresa.cep
        dados["estado"] = empresa.estado
        dados["cidade"] = empresa.cidade
        dados["endereco"] = empresa.endereco
        dados["dt_cadastro"] = empresa.data_cadastro
        dados["validade_contrato"] = empresa.data_fim_contrato 
        return dados
    else:
        return False
    

def RegistrarServicoDb(registrarservico, usuario):
    referencia = Empresassocias.query.filter_by(cnpj=registrarservico.cnpj.data).first()
    id_empresa = Empresassocias.query.get(referencia.id_empresa)
    novoservico = Servicosdisponiveis(nome_servico=registrarservico.servico.data.upper(),
                                      desconto=registrarservico.desconto.data,
                                      user_cadastro=usuario.email.upper(),
                                      empresa=id_empresa,
                                      )
    db.session.add(novoservico)
    db.session.commit()
    return {"message": "Registrado com sucesso", "status_notificacao": "alert-success"}

