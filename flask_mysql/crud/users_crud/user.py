from mysqlconnection import connectToMySQL

class User:
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def retrieve_users(cls):
        query = "SELECT * FROM users"
        
        result = connectToMySQL('users_schema').query_db(query)
        
        users = []
        for user in result:
            users.append(cls(user))
        return users
    
    @classmethod
    def insert_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at) VALUES (%(first_name)s,%(last_name)s,%(email)s, NOW());"
        return connectToMySQL('users_schema').query_db(query, data)
    
    @classmethod
    def select_user(cls,data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)
    
    @classmethod
    def update_user(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL('users_schema').query_db(query, data)
    
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s"
        return connectToMySQL('users_schema').query_db(query, data)
