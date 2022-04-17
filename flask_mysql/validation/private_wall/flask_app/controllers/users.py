from flask_app import app, bcrypt
from flask import render_template, request, redirect, url_for, session

from flask_app.models.user import User

# Display routes
@app.route('/')
def index():
    return redirect('/dashboard')
    # return render_template('index.html')

# @app.route('/dashboard')
# def showDashboard():
#     if 'remember' in session:
#         if 'uuid' in session:
#             data = {
#                 "id" : session['uuid']
#             }
#             user = User.select(data)
#             if session['remember'] == 'off':
#                 del session['uuid']
#                 del session['remember']
#             return render_template('dashboard.html', user=user)
#     return redirect('/')

@app.route('/logout')
def logout():
    if 'uuid' in session:
        del session['uuid']
    if 'remember' in session:
        del session['remember']
    return redirect('/')

# Action routes
@app.route('/process/registration', methods=["POST"])
def processRegistration():
    if not User.validate_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        'password': pw_hash,
    }
    user = User.insert(data)
    session['uuid'] = user
    session['remember'] = 'off'
    return redirect('/dashboard')

@app.route('/process/login', methods=["POST"])
def processLogin():
    if 'remember' in request.form:
        session['remember'] = request.form['remember']
    else:
        session['remember'] = 'off'
    # check if there is a user
    if "uuid" not in session:
        if not User.validate_login(request.form):
            return redirect('/')
    # see if there is a new user input even when remember was checked
    if request.form['email'] != "" and request.form['password'] != "":
        if not User.validate_login(request.form):
            return redirect('/')
    return redirect('/dashboard')

