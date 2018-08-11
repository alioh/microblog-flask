from flask import Flask
from config import Config
#from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager

micro = Flask(__name__)
micro.config.from_object(Config)
#Bootstrap(micro)
db = SQLAlchemy(micro)
migrate = Migrate(micro, db)
login = LoginManager(micro)
login.login_view = 'login'

from app import routes, models