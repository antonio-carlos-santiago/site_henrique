from bs4 import BeautifulSoup
from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user, login_required
from requests import Session

from henrique import app, db, bcrypt
from henrique.formularios import Login_sis, Novo_contracheque, Consulta_Prodan, Novo_user, Consulta_Consiglog
from henrique.modelos import Usuarios


@app.route('/principal')
@login_required
def Home():
    return render_template('principal.html')


@app.route('/', methods=['post', 'get'])
def Login():
    login_sis = Login_sis()
    if login_sis.validate_on_submit() and 'btn_login' in request.form:
        usuario = Usuarios.query.filter_by(email=login_sis.email.data).first()
        print(usuario.senha)
        if usuario and bcrypt.check_password_hash(usuario.senha, login_sis.senha.data):
            login_user(usuario)
            flash('Logado com sucesso', 'alert-success')
            return redirect(url_for('Home'))
        else:
            flash('Dados não conferem!', 'alert-danger')

    return render_template('login.html', login_sis=login_sis)


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
