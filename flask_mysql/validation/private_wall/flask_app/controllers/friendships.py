from flask_app import app, bcrypt
from flask import render_template, request, redirect, url_for, session

from flask_app.models.friendship import Friendship

@app.route('/friendships')
def info():
    data = {
        "user_id": 1,
        "friend_id": 2
    }
    info = Friendship.get_messages_from(data)
    print(info.messages)
    return redirect('/')

@app.route('/dashboard')
def showDashboard():
    # if 'remember' in session:
    #     if 'uuid' in session:
    #         data = {
    #             "id" : session['uuid']
    #         }
    #         user = User.select(data)
    #         if session['remember'] == 'off':
    #             del session['uuid']
    #             del session['remember']
    #         return render_template('dashboard.html', user=user)
    data = {
        "user_id": 1,
    }
    message = Friendship.get_messages_from(data)
    print(message)
    friends = Friendship.get_all_friend(data)
    print(friends)
    return render_template('dashboard.html', messages=message, friends=friends)