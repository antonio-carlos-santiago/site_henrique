from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


class Base(DeclarativeBase):
    pass

app = Flask(__name__)

app.secret_key = 'queroumkuvaimedar?'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:FgaGBG5BfA6D26CGda51G-c1Ebb1*53C@viaduct.proxy.rlwy.net:50457/railway'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

db = SQLAlchemy(model_class=Base)

db.init_app(app)
login_manager = LoginManager()

from henrique import modelos

with app.app_context():
    db.drop_all()
    db.create_all()

bcrypt = Bcrypt(app)
login_manager.init_app(app)

login_manager.login_view = 'Login'
login_manager.login_message = 'Faça login para continuar'
login_manager.login_message_category = 'alert-info'


from henrique import rotas
