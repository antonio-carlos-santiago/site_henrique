from henrique.modelos import *
from henrique import db, app
from datetime import datetime, timedelta



def RegistarEmpresa(dadosempresa):
    data_final_contrato = datetime.now() + timedelta(days=int(dadosempresa.adesao.data) * 365)
    empresa_cadastrada = Empresassocias(nome=dadosempresa.nome.data.upper(),
                                        cnpj=dadosempresa.cnpj.data,
                                        cep=dadosempresa.cep.data,
                                        estado=dadosempresa.estado.data,
                                        cidade=dadosempresa.cidade.data,
                                        endereco=dadosempresa.endereco.data.upper(),
                                        numero_residencia=dadosempresa.numero_residencia.data,
                                        data_fim_contrato=data_final_contrato
                                        )
    
    db.session.add(empresa_cadastrada)
    db.session.commit()
    return {"message": "Empresa registrada com sucesso", "status_notificacao": "alert-info"}
    
    
