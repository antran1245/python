from flask import Flask

app = Flask(__name__)
app.secret_key = "survey_dojo"

from flask_app.controllers import dojos