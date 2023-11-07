import os
from hashlib import md5
from flask_login import LoginManager
from flask import Flask, render_template

from blueprints.dashboard_blueprint import dashboard_blueprint
from blueprints.home_blueprint import home_blueprint
from blueprints.login_blueprint import login_blueprint
from db import DBConnector
from db.model import Produtos
from db.model.usuarios import Usuarios

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

app.register_blueprint(home_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(dashboard_blueprint)


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return str(Usuarios().get_by_id(user_id))

def init_database():
    with DBConnector.get_session() as session:
        Produtos()
        Usuarios()

    try:
        user = Usuarios()
        user.id = 1
        user.user = 'admin'
        senha = "admin123"
        user.senha = md5(senha.encode()).hexdigest()
        e = session.query(Usuarios).filter(Usuarios.id == 1).first()
        if e is None:
            session.add(user)
            session.commit()
    except Exception as e:
        session.rollback()
        print(e)


init_database()

app.run(host='0.0.0.0', debug=True)