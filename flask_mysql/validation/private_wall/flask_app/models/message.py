from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE;
from flask import flash
class Message:
    
    def __init__(self, data):
        self.id = data['id']
        self.friendship_id = data['friendship_id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM messages"
        result = connectToMySQL(DATABASE).query_db(query)
        tables = []
        for table in result:
            tables.append(cls(table))
        return tables
    
    @classmethod
    def insert(cls, data):
        query = "INSERT INTO messages (friendship_id, content) VALUES (%(friendship_id)s,%(content)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def select(cls,data):
        query = "SELECT * FROM messages WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE messages SET friendship_id=%(friendship_id)s, content=%(content)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM messages WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def validate_send_message(data, id):
        is_valid = True
        if len(data['message']) < 5:
            print("wwwwwwwwwwwwwwehhe")
            flash("Message need to have a minimum of 5 chars.", id)
            is_valid = False
        return is_valid