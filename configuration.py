from flask import Flask
from pony.flask import Pony
from flask_jwt_extended import JWTManager
from model import db

app = Flask(__name__)

jwt = JWTManager(app)
ponyapp = Pony(app)