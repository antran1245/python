from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "loginREgristation"
bcrypt = Bcrypt(app)
DATABASE = 'private_wall_schema'
from flask_app.controllers import users, friendships