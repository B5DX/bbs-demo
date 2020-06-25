from flask import Flask
from app.config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config.from_object(Config)
login = LoginManager(app)
db = SQLAlchemy(app)
