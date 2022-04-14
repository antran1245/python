from flask_app import app
from flask import render_template, redirect, request, url_for

from flask_app.models.author import Author
from flask_app.models.book import Book

# Display routes
@app.route('/books')
def books():
    books = Book.get_all()
    return render_template('books.html', books=books)

@app.route('/book/<int:id>')
def showBook(id):
    data = {
        "id" : id
    }
    book = Book.select(data)
    favorites = Book.showFavorite(data)
    notFavorites = Book.notFavorite(data)
    return render_template('showBook.html', book=book, favorites=favorites, notFavorites=notFavorites)


# Action routes
@app.route('/process/add/book', methods={"POST"})
def processAddBook():
    data = {
        "title": request.form['name'],
        "num_of_pages": request.form['pages']
    }
    Book.insert(data)
    return redirect('/books')
