from flask import Blueprint, render_template, abort
from flask_login import login_required

dashboard_blueprint = Blueprint('dashboard_blueprint', __name__,
                        template_folder='templates')

@login_required
@dashboard_blueprint.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')