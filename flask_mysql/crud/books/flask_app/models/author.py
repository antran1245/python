from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
database = "books_schema"
class Author:
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors"
        
        result = connectToMySQL(database).query_db(query)
        
        authors = []
        for author in result:
            authors.append(cls(author))
        return authors
    
    @classmethod
    def insert(cls, data):
        query = "INSERT INTO authors (name, created_at) VALUES (%(name)s,NOW());"
        return connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def select(cls,data):
        query = "SELECT * FROM authors WHERE id=%(id)s;"
        return connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE authors SET name=%(name)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM authors WHERE id=%(id)s"
        return connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def showFavorite(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id=favorites.author_id LEFT JOIN books ON books.id=favorites.book_id WHERE authors.id=%(id)s;"
        result = connectToMySQL(database).query_db(query, data)
        books = []
        for row in result:
            book_data = {
                "id" : row['id'],
                "title" : row['title'],
                "num_of_pages" : row['num_of_pages'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            books.append(book.Book(book_data))
        return books
    
    @classmethod
    def notFavorite(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id=favorites.author_id LEFT JOIN books ON books.id=favorites.book_id WHERE authors.id=%(id)s;"
        result = connectToMySQL(database).query_db(query, data)
        books = []
        all_books = book.Book.get_all()
        for one_book in all_books:
            book_exist = False
            for row in result:
                if(one_book.id == row['book_id']):
                    book_exist = True
            if not book_exist:    
                books.append(one_book)
        return books