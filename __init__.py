import os
from flask import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()
app = Flask(__name__)

######################## DATABASE ###############

basedir = os.path.abspath(os.path.dirname(__file__))
app.app_context().push()

app.config["SECRET_KEY"] = "secretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)
login_manager.init_app(app)
login_manager.login_view = 'login'

