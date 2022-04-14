from flask_app.config.mysqlconnection import connectToMySQL
database='books_schema'
class Favorite:
    
    def __init__(self, data):
        self.author_id = data['author_id']
        self.book_id = data['book_id']
    
    @classmethod
    def insert(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL(database).query_db(query, data)