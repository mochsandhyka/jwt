from flask import Flask,request,jsonify
from pony.flask import Pony
from flask_jwt_extended import JWTManager,jwt_required,current_user,create_access_token,get_jwt_identity
from model import db
import os,uuid,hashlib,re
from http import HTTPStatus
 

app = Flask(__name__)


app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
email_regex = re.compile(r"[^@]+@[^@]+\.[^@]")


myId = uuid.uuid4()
jwt = JWTManager(app)
ponyapp = Pony(app)