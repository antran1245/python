from flask_app import app
from flask import render_template, redirect, request, url_for

from flask_app.models.favorite import Favorite

# Action routes
@app.route('/process/add/book/add/<int:id>', methods=['POST'])
def processAddBookFavorite(id):
    data = {
        "author_id" : request.form['author'],
        "book_id" : id
    }
    Favorite.insert(data)
    print('here')
    return redirect(url_for('showBook', id=id))

@app.route('/process/add/author/add/<int:id>', methods=['POST'])
def processAddAuthorFavorite(id):
    data = {
        "book_id" : request.form['book'],
        "author_id" : id
    }
    Favorite.insert(data)
    print('here')
    return redirect(url_for('showAuthor', id=id))