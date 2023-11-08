from henrique.modelos import *
from henrique import db
from datetime import datetime, timedelta



def RegistarEmpresa(dadosempresa):
    data_final_contrato = datetime.now() + timedelta(days=int(dadosempresa.adesao.data) * 365)
    empresa_cadastrada = Empresassocias(nome=dadosempresa.nome.data,
                                        cnpj=dadosempresa.cnpj.data,
                                        cep=dadosempresa.cep.data,
                                        estado=dadosempresa.estado.data,
                                        cidade=dadosempresa.cidade.data,
                                        endereco=dadosempresa.endereco.data,
                                        numero_residencia=dadosempresa.numero_residencia.data,
                                        data_fim_contrato=data_final_contrato
                                        )
    
    db.session.add(empresa_cadastrada)
    db.session.commit()
    return {"message": "Empresa registrada com sucesso", "status_notificacao": "alert-info"}
    
    
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
    novoservico = ServicosDisponiveis(nome_servico=registrarservico.servico.data,
                                      desconto=registrarservico.desconto.data,
                                      user_cadastro=usuario.email,
                                      empresa=id_empresa,
                                      )
    db.session.add(novoservico)
    db.session.commit()
    return {"message": "Registrado com sucesso", "status_notificacao": "alert-success"}
