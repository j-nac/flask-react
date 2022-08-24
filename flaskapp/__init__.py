from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt import JWT
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
api = Api(app)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Import db then db.create_all() to generate sqlite file
db = SQLAlchemy(app)

# Runs password through sha256 before using secure hashing algorithm to handle passwords of any length
app.config['BCRYPT_HANDLE_LONG_PASSWORDS'] = True
bcrypt = Bcrypt(app)

from flaskapp.auth import authenticate, identity

jwt = JWT(app, authenticate, identity)

from flaskapp import resources