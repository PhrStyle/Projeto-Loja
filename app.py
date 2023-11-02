from hashlib import md5

from flask import Flask, render_template

from blueprints.home_blueprint import home_blueprint
from db import DBConnector
from db.model import Produtos
from db.model.usuarios import Usuarios

app = Flask(__name__)

app.register_blueprint(home_blueprint)

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