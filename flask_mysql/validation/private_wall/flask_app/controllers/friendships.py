from flask_app import app, bcrypt
from flask import render_template, request, redirect, url_for, session

from flask_app.models.friendship import Friendship
from flask_app.models.user import User

@app.route('/dashboard')
def showDashboard():
    if 'remember' in session:
        if 'uuid' in session:
            data = {
                "user_id" : session['uuid']
            }
            user = User.get_name(data)
            if session['remember'] == 'off':
                del session['uuid']
                del session['remember']
            message = Friendship.get_messages_from(data)
            friends = Friendship.get_all_friend(data)
            possibles = User.get_all_possible_friends(data)
            return render_template('dashboard.html', messages=message, friends=friends, user=user, possibles=possibles)
    return redirect('/')

@app.route('/addFriend/<int:user>/<int:friend>')
def addFriendship(user, friend):
    data = {
        "user_id": user,
        "friend_id": friend
    }
    Friendship.insert(data)
    data = {
        "user_id": friend,
        "friend_id": user
    }
    Friendship.insert(data)
    return redirect('/dashboard')