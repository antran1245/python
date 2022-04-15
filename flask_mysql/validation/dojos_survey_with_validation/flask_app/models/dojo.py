from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

database='dojo_survey_schema'

class Dojo:
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        
        result = connectToMySQL(database).query_db(query)
        
        dojos = []
        for dojo in result:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def insert(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s,%(location)s,%(language)s, %(comment)s);"
        return connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def select(cls,data):
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        return connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s, location=%(location)s, language=%(language)s, comment=%(comment)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojos WHERE id=%(id)s"
        return connectToMySQL(database).query_db(query, data)
    
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if(dojo['name'] == ""):
            flash('Require a name.')
            is_valid = False
        if(dojo['location'] == 'default'):
            flash('Select a location.')
            is_valid = False
        if(dojo['language'] == 'default'):
            flash('Select a language.')
            is_valid = False
        return is_valid