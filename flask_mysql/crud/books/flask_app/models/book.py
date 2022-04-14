from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
database = "books_schema"
class Book:
    
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books"
        
        result = connectToMySQL(database).query_db(query)
        
        books = []
        for book in result:
            books.append(cls(book))
        return books
    
    @classmethod
    def insert(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at) VALUES (%(title)s,%(num_of_pages)s, NOW());"
        return connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def select(cls,data):
        query = "SELECT * FROM books WHERE id=%(id)s;"
        return connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE books SET title=%(title)s, num_of_pages=%(num_of_pages)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM books WHERE id=%(id)s"
        return connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def showFavorite(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id=favorites.book_id LEFT JOIN authors ON authors.id=favorites.author_id WHERE books.id=%(id)s;"
        result = connectToMySQL(database).query_db(query, data)
        authors = []
        for row in result:
            author_data = {
                "id" : row['id'],
                "name" : row['name'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            authors.append(author.Author(author_data))
        return authors
    
    @classmethod
    def notFavorite(cls,data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id=favorites.book_id LEFT JOIN authors ON authors.id=favorites.author_id WHERE authors.id=%(id)s;"
        result = connectToMySQL(database).query_db(query, data)
        authors = []
        all_authors = author.Author.get_all()
        for one_author in all_authors:
            author_exist = False
            for row in result:
                if(one_author.id == row['author_id']):
                    author_exist = True
            if not author_exist:    
                authors.append(one_author)
        return authors