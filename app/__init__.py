from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

micro = Flask(__name__)
micro.config.from_object(Config)
Bootstrap(micro)
db = SQLAlchemy(micro)
migrate = Migrate(micro, db)


from app import routes, models