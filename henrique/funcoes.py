from henrique.modelos import *
from henrique import db
from datetime import datetime, timedelta



def RegistarEmpresa(dadosempresa):
    data_final_contrato = datetime.now() + timedelta(days=int(dadosempresa.adesao.data) * 365)
    empresa_cadastrada = EmpresasSocias(nome=dadosempresa.nome.data,
                                        cnpj=dadosempresa.cnpj.data,
                                        cep=dadosempresa.cep.data,
                                        estado=dadosempresa.estado.data,
                                        cidade=dadosempresa.cidade.data,
                                        endereco=dadosempresa.endereco.data,
                                        numero_residencia=dadosempresa.numero_residencia.data,
                                        servico=dadosempresa.servico.data,
                                        desconto=dadosempresa.desconto.data,
                                        data_fim_contrato=data_final_contrato
                                        )
    try:
        db.session.add(empresa_cadastrada)
        db.session.commit()
        return {"message": "Empresa registrada com sucesso", "status_notificacao": "alert-info"}
    
    except Exception as erro:
        print(erro)
        return {"message": "Erro ao registrar empresa", "status_notificacao": "alert-danger"}
