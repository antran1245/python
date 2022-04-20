from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re
from flask_app import bcrypt, DATABASE

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'(?=.*[0-9])(?=.*[A-Z])([A-Za-z0-9]+)')
class User:
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        
        result = connectToMySQL(DATABASE).query_db(query)
        
        users = []
        for user in result:
            users.append(cls(user))
        return users
    
    @classmethod
    def insert(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def select(cls,data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def validate_email_exist(data):
        query = "SELECT * From users WHERE email=%(email)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return True
        return False
        
    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len(data['first_name']) < 3:
            flash("First Name must be at least 2 characters.", 'user_first_name_error')
            is_valid = False
        if not data['first_name'].isalpha():
            flash("First Name must be in letters only.", 'user_first_name_error')
            is_valid = False
        if len(data['last_name']) < 3:
            flash("Last Name must be at least 2 characters.", 'user_last_name_error')
            is_valid = False
        if not data['last_name'].isalpha():
            flash("Last Name must be in letters only.", 'user_last_name_error')
            is_valid = False
        if len(data['password']) < 8:
            flash('Password need to be at least 8 characters.', 'user_password_error')
            is_valid = False
        if not PASSWORD_REGEX.match(data['password']):
            flash('Password require 1 Uppercase and 1 Number.', 'user_password_error')
            is_valid = False
        if data['password'] != data['confirm']:
            flash('Password does not match.', 'user_confirm_password_error')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('Email is not valid.', 'user_email_error')
            is_valid = False
        if not User.validate_email_exist(data):
            flash('Email exist.', 'user_email_error')
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        if len(data['password']) < 8:
            flash('Password need to be at least 8 characters.', 'login_password_error')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('Email is not valid.', 'login_email_error')
            is_valid = False
        if User.validate_email_exist(data):
            flash('Email does not exist.', 'login_email_error')
            is_valid = False
        elif User.check_password(data):
            flash('Invalid password.', 'login_password_error')
            is_valid = False
        return is_valid
    
    @staticmethod
    def check_password(data):
        query = "SELECT * From users WHERE email=%(email)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return True
        if bcrypt.check_password_hash(result[0]['password'], data['password']):
            session['uuid'] = result[0]['id']
            return False
        return True