from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
database='email_schema'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Email:
    
    def __init__(self, data):
        self.id = data['id']
        self.address = data['address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails"
        
        result = connectToMySQL(database).query_db(query)
        
        addresses = []
        for addresse in result:
            addresses.append(cls(addresse))
        return addresses
    
    @classmethod
    def insert(cls, data):
        query = "INSERT INTO emails (address, created_at) VALUES (%(address)s, NOW());"
        return connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def select(cls,data):
        query = "SELECT * FROM emails WHERE id=%(id)s;"
        return connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE emails SET address=%(address)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM emails WHERE id=%(id)s"
        return connectToMySQL(database).query_db(query, data)
    
    @staticmethod
    def validation_email(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address!', 'error')
            is_valid = False
        return is_valid