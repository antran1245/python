from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
class Recipe:
    
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.description = data['description']
        self.time = data['time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes"
        result = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for recipe in result:
            recipes.append(cls(recipe))
        return recipes
    
    @classmethod
    def insert(cls, data):
        query = "INSERT INTO recipes (user_id, description, time) VALUES (%(user_id)s,%(description)s,%(time)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def select(cls,data):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET user_id=%(user_id)s, description=%(description)s, time=%(time)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_all_from_user(cls, data):
        query = "SELECT * FROM recipes WHERE user_id=%(user_id)s"
        result - connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for recipe in result:
            recipes.append(cls(recipe))
        return recipes