from flask_app import app
from flask import render_template,redirect,request,session, url_for

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

# Display Route
@app.route('/')
def main():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('dojos.html', dojos=dojos) 

@app.route('/ninjas')
def create_ninja():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos=dojos)

@app.route('/dojo/<int:id>')
def showDojo(id):
    data = {
        "dojo_id": id
    }
    ninjas = Ninja.dojo_ninjas(data)
    dojo = Dojo.read_dojo(data)
    print(ninjas)
    return render_template('dojo_show.html', ninjas=ninjas, dojo=dojo)

# Action route
@app.route('/process/create/dojos', methods=['POST'])
def processCreateDojos():
    data = {
        "name": request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect('/')

@app.route('/process/ninja', methods=['POST'])
def addNinja():
    data = {
        "dojo_id" : request.form['dojo'],
        "fname" : request.form['fname'],
        "lname" : request.form['lname'],
        "age" : request.form['age']
    }
    Ninja.create_ninja(data)
    return redirect(url_for('showDojo', id=request.form['dojo']))