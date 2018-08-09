from flask import Flask
from config import Config

micro = Flask(__name__)
micro.config.from_object(Config)

from app import routes