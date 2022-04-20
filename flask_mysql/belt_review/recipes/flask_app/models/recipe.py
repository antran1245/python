from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask_app.models import user
from flask import flash
class Recipe:
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.user_id = data['user_id']
        self.description = data['description']
        self.instructions = data['instructions']
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
        query = "INSERT INTO recipes (user_id, name, description, instructions, time) VALUES (%(user_id)s, %(name)s, %(description)s,%(instructions)s,%(time)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def select(cls,data):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s time=%(time)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_all_from_user(cls, data):
        query = "SELECT * FROM recipes WHERE user_id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        chief = user.User.select(data)
        for recipe in result:
            chief.recipes.append(cls(recipe))
        return chief
    
    @staticmethod
    def get_one_from_user(data):
        query = "SELECT * FROM recipes JOIN users ON user_id = users.id WHERE recipes.id=%(recipe_id)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        returnData = {
            "id": result[0]['id'],
            "name" : result[0]['name'],
            "description" : result[0]['description'],
            "instructions" : result[0]['instructions'],
            "time" : result[0]['time'],
            "created_at" : result[0]['created_at'],
            "first_name" : result[0]['first_name']
        }
        return returnData
    
    @staticmethod
    def validate_input(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Name need at least 3 characters.", "err_name")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description need at least 3 characters.", "err_description")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Instructions need at least 3 characters.", "err_instructions")
            is_valid = False
        if data['created_at'] == "":
            flash("Require a date.", "err_date")
            is_valid = False
        if "time" not in data:
            flash("Yes or No on Under 30 Minutes.", "err_time")
            is_valid = False
        return is_valid