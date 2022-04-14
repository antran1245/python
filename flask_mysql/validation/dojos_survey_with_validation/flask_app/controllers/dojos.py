from flask_app import app
from flask import render_template,redirect,request,session, url_for

from flask_app.models.dojo import Dojo

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/process', methods=["POST"])
def process():
    # if request.form["name"] != "":
    #     session["name"] = request.form["name"]
    # if request.form["location"] != "default":
    #     session["location"] = request.form["location"]
    # if request.form["language"] != "default":
    #     session["language"] = request.form["language"]
    # if request.form["comment"] != "":
    #     session["comment"] = request.form["comment"]
    if "radioColor" in request.form:
        session["color"] = request.form['radioColor']
    if "checkFood" in request.form:
        session["food"] = request.form['checkFood']
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    survey = Dojo.insert(request.form)
    
    return redirect(url_for('result', id=survey))

@app.route('/result/<int:id>')
def result(id):
    data = {"id": id}
    filled = Dojo.select(data)
    return render_template('result.html', info=filled)

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')