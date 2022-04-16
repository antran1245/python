from flask_app import app
from flask import render_template,redirect,request,session, url_for

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

# Display Routes
@app.route('/')
def main():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos=dojos) 

@app.route('/ninjas')
def create_ninja():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos=dojos)

@app.route('/dojo/<int:id>')
def showDojo(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_all_ninjas(data)
    return render_template('dojo_show.html', dojo=dojo)

# Action/form routes 
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