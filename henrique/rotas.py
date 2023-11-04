from flask import render_template, request, redirect, flash, url_for, session
from flask_login import login_user, logout_user, login_required
from requests import Session
from henrique import app, db, bcrypt
from henrique.formularios import Login_sis, Novo_user, NovaEmpresa
from henrique.modelos import Usuarios
import time


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
        pass



    return render_template('cadastro_empresa.html', novaempresa=novaempresa)



@app.route('/novo-usuario', methods=['post', 'get'])
@login_required
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
