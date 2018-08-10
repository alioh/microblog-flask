from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

micro = Flask(__name__)
micro.config.from_object(Config)
Bootstrap(micro)

from app import routes