from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "recipes_schema"
bcrypt = Bcrypt(app)
DATABASE = "recipes_schema"
from flask_app.controllers import users, recipes