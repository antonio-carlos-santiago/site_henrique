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
        dados["nome"] = empresa.nome
        dados["cep"] = empresa.cep
        dados["estado"] = empresa.estado
        dados["cidade"] = empresa.cidade
        dados["endereco"] = empresa.endereco
        dados["status"] = empresa.status
        return dados
    
