from flask_app import app
from flask import render_template, redirect, request, url_for

from flask_app.models.author import Author
from flask_app.models.book import Book

# Display routes
@app.route('/')
def main():
    return redirect('/authors')

@app.route('/authors')
def authors():
    authors = Author.get_all()
    return render_template('authors.html', authors=authors)

@app.route('/author/<int:id>')
def showAuthor(id):
    data = {
        "id": id
    }
    books = Author.showFavorite(data)
    author = Author.select(data)
    notFavorites = Author.notFavorite(data)
    return render_template('showAuthor.html', books=books, author=author, notFavorites=notFavorites)


# Action routes
@app.route('/process/add/author', methods=["POST"])
def processAddAuthor():
    data = {
        "name": request.form['name']
    }
    Author.insert(data)
    return redirect('/')