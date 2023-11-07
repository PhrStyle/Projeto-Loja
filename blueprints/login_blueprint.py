from hashlib import md5

from flask import Blueprint, render_template, abort, request

from db.model.usuarios import Usuarios

login_blueprint = Blueprint('login_blueprint', __name__,
                        template_folder='templates')

@login_blueprint.route("/login")
def login():
    return render_template('login.html')

@login_blueprint.route("/authenticate", methods =["POST"])
def authenticate():
    email = request.args.get('email')
    senha = md5(request.args.get('senha').encode()).hexdigest()
    usuario = Usuarios()
    ret = usuario.get_usuario_by_user(email)
    if ret is not None:
        if senha == ret.senha:
            return "0"
        else:
            return "2"
    else:
        return "1"