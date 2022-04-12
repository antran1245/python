from flask import Flask, render_template, request, redirect
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
        User.insert_user(data)
        return redirect('/users')

@app.route('/users/new')
def userForm():
    return render_template('new_user.html')

if __name__=="__main__":
    app.run(debug=True)