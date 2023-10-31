from flask import Flask, render_template

from blueprints.home_blueprint import home_blueprint

app = Flask(__name__)

app.register_blueprint(home_blueprint)



app.run(host='0.0.0.0', debug=True)