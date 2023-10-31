from flask import Blueprint, render_template, abort

home_blueprint = Blueprint('home_blueprint', __name__,
                        template_folder='templates')

@home_blueprint.route("/")
def hello_world():
    return render_template('home.html',
                           )