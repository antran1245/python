from flask import Flask
app = Flask(__name__)
app.secret_key = "emails YEAH VALID"

from flask_app.controllers import emails