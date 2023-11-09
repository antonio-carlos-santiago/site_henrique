from flask import render_template, request, redirect, flash, url_for, session
from flask_login import login_user, logout_user, login_required, current_user
from henrique import app, db, bcrypt
from henrique.formularios.forms_cliente import *
from henrique.formularios.forms_empresa import *
from henrique.formularios.forms_site import *
from henrique.modelos import Usuarios
import time
from henrique.funcoes.funcoes_cadastro_empresa import *
from henrique.funcoes.funcoes_cadastro_servico import *
from henrique.funcoes.funcoes_status_alteracao import *



@app.before_request
def session_management():
    session.permanent = True
    app.permanent_session_lifetime = app.config['PERMANENT_SESSION_LIFETIME']
    
    if 'last_activity' in session:
        elapsed_time = time.time() - session['last_activity']
        if elapsed_time > app.config['PERMANENT_SESSION_LIFETIME']:
            # A sessão expirou; você pode redirecionar o usuário para uma página de login
            return redirect(url_for('Login'))
    session['last_activity'] = time.time()


@app.route('/principal')
@login_required
def Home():
    return render_template('principal.html')


@app.route('/', methods=['post', 'get'])
def Login():
    logout_user()
    login_sis = Login_sis()
    if login_sis.validate_on_submit() and 'btn_login' in request.form:
        usuario = Usuarios.query.filter_by(email=login_sis.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, login_sis.senha.data):
            login_user(usuario)
            flash('Logado com sucesso', 'alert-success')
            return redirect(url_for('Home'))
        else:
            flash('Dados não conferem!', 'alert-danger')

    return render_template('login.html', login_sis=login_sis)



@app.route("/cadastrar-empresa", methods=["post", "get"])
@login_required
def CadastrarEmpressa():
    novaempresa = NovaEmpresa()
    if novaempresa.validate_on_submit() and "btn_cadastrar_empresa" in request.form:
        status = RegistarEmpresa(novaempresa)
        flash(status["message"], status["status_notificacao"])

    return render_template('cadastro_empresa.html', novaempresa=novaempresa)


@app.route("/cadastrar-servico", methods=["get", "post"])
@login_required
def CadastrarServico():
    buscarempresa = BuscarEmpresa()
    registrarservico = RegistrarServico()
    if buscarempresa.validate_on_submit() and "btn_busca" in request.form:
        registrarservico.cnpj.data = buscarempresa.cnpj.data
        status = BuscarEmpresaDb(buscarempresa.cnpj.data)
        return render_template("cadastro_servico_empresa.html", buscarempresa=buscarempresa, status=status, registrarservico=registrarservico)

    if registrarservico.validate_on_submit() and "btn_reg_serv" in request.form:
        adicionando_servico = RegistrarServicoDb(registrarservico, current_user)
        flash(adicionando_servico['message'], adicionando_servico['status_notificacao'])
            
    return render_template("cadastro_servico_empresa.html", buscarempresa=buscarempresa, registrarservico=registrarservico)
    



@app.route("/verificar-alterar-status", methods=["get", "post"])
@login_required
def Verificar_Alterar_Status():
    form_empresas = BuscarEmpresas()
    form_atualizacao = AtualizacaoEmpresa()
    form_empresas_serv = BuscarEmpresas()
    form_buscaservicos = BuscarServicos()

    if form_empresas.validate_on_submit() and 'btn_conf' in request.form:
        lista_servicos = BuscaServicosDb(form_empresas.empresas.data)
        form_buscaservicos.servicos.choices = lista_servicos

        print(form_empresas.empresas.data)

        status = PesquisaPorEmpresa(form_empresas.empresas.data)
        form_atualizacao.nome_origem.data = form_empresas.empresas.data
        form_atualizacao.nome.data = status['nome']
        form_atualizacao.status.data = status['status']
        form_atualizacao.cep.data = status['cep']
        form_atualizacao.estado.data = status['estado']
        form_atualizacao.cidade.data = status['cidade']
        form_atualizacao.endereco.data = status['endereco']
        form_atualizacao.numero_residencia.data = status['numero_residencia']
        form_atualizacao.telefone.data = status['telefone']
        return render_template(
            "verificar_alterar_status.html",
             form_empresas=form_empresas,
             form_atualizacao=form_atualizacao,
             form_buscaservicos=form_buscaservicos,
             )
    

    
    if form_atualizacao.validate_on_submit() and "btn_atualizar_empresa" in request.form:
        status = AtualizarDadosCadastrais(form_atualizacao)
        flash(status['message'], status['status_notificacao'])



    return render_template(
        "verificar_alterar_status.html",
        form_empresas=form_empresas,
        form_atualizacao=form_atualizacao,
        form_buscaservicos=form_buscaservicos,
        form_empresas_serv=form_empresas_serv
        )





@app.route('/novo-usuario', methods=['post', 'get'])
#@login_required
def Criar_Acesso():
    novo_usuario = Novo_user()
    if novo_usuario.validate_on_submit() and 'btn_criar' in request.form:
        senha_crypt = bcrypt.generate_password_hash(novo_usuario.nova_senha.data)
        usuario = Usuarios(email=novo_usuario.email.data, senha=senha_crypt)
        db.session.add(usuario)
        db.session.commit()
        flash('Usuario cadastrado com sucesso', 'alert-info')

    return render_template('novo_usuario.html', novo_usuario=novo_usuario)





@app.route('/Sair')
@login_required
def Sair():
    logout_user()
    flash('Desconectado com sucesso, Faça login para continuar.', 'alert-success')
    return redirect(url_for('Login'))
