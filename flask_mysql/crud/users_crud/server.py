from flask import Flask, render_template, request, redirect, url_for
from user import User

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.retrieve_users()
    return render_template('users.html', users=users)

@app.route('/process', methods=['POST'])
def process():
    if request.method == "POST":
        #return render_template('users.html')
        data = {
            "first_name": request.form['fname'],
            "last_name": request.form['lname'],
            "email": request.form['email'],
        }
        user = User.insert_user(data)
        return redirect(url_for('showUser', user=user))

@app.route('/users/new')
def userForm():
    return render_template('new_user.html')

# @app.errorhandler(404)
# def page_not_found(e):
#     print('404')
#     return redirect('/users')

@app.route('/users/<int:user>')
def showUser(user):
    data = {
        "id": user
    }
    user = User.select_user(data)
    print(user)
    return render_template('show_user.html', user=user)

@app.route('/users/<int:user>/edit')
def editUser(user):
    data = {
        "id": user
    }
    user = User.select_user(data)
    return render_template('edit_user.html', user=user)

@app.route('/process/edit', methods=['POST'])
def processEdit():
    if request.method == "POST":
        data = {"id": int(request.form['id'])}
        user = User.select_user(data)
        if((request.form['fname'] != user[0]['first_name']) or (request.form['lname'] != user[0]['last_name']) or (request.form['email'] != user[0]['email'])):
            data = {
                "first_name": request.form['fname'],
                "last_name": request.form['lname'],
                "email": request.form['email'],
                "id": int(request.form['id'])
            }
            User.update_user(data)
            return redirect(url_for('showUser', user=user[0]['id']))
    return redirect(url_for('editUser', user=user[0]['id']))

@app.route('/delete/<int:user>')
def deleteUser(user):
    data = {"id":user}
    User.delete_user(data)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)