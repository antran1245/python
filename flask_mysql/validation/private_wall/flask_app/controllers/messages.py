from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.message import Message
from flask_app.models.friendship import Friendship

@app.route('/message/remove/<int:id>')
def removeMessage(id):
    data = {
        "id" : id
    }
    Message.delete(data)
    return redirect('/dashboard')

@app.route('/send/<int:user_id>/<int:friend_id>', methods=['POST'])
def sendMessage(user_id, friend_id):
    data = {
        "user_id": user_id,
        "friend_id" : friend_id,
    }
    friendship_id = Friendship.get_friendship_id(data)
    data = {
        "friendship_id": friendship_id,
        "content": request.form['message']
    }
    if Message.validate_send_message(request.form, friend_id):
        Message.insert(data)
    return redirect('/dashboard')
