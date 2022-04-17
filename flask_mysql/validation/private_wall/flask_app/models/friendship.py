from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.message import Message
class Friendship:
    
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM friendships;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        tables = []
        for table in result:
            tables.append(cls(table))
        return tables
    
    @classmethod
    def insert(cls, data):
        query = "INSERT INTO friendships (user_id, friend_id) VALUES (%(user_id)s,%(friend_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def select(cls,data):
        query = "SELECT * FROM friendships WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE friendships SET user_id=%(user_id)s, friend_id=%(friend_id)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM friendships WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # Get all the friends for that user
    @classmethod
    def get_all_friend(cls, data):
        query = "SELECT * FROM friendships LEFT JOIN users ON friendships.friend_id = users.id WHERE user_id=%(user_id)s GROUP BY users.id;"        
        result = connectToMySQL(DATABASE).query_db(query, data)
        users = []
        for user in result:
            data = {
                "id" : user['users.id'],
                "friend_id" : user['friend_id'],
                "friend_first_name": user['first_name'],
                "friend_last_name" : user['last_name'],
                "created_at" : user['created_at'],
                "updated_at" : user['updated_at']
            }
            users.append((data))
        return users
    
    # @classmethod
    # def get_messages_from(cls, data):
    #     query = "SELECT * FROM friendships WHERE user_id=%(user_id)s AND friend_id=%(friend_id)s;"
    #     result = connectToMySQL(DATABASE).query_db(query, data)
    #     friendship = cls(result[0])
    #     data = {"friendship_id": friendship.id}
    #     return Message.get_all_messages(data)
    
    @classmethod
    def get_messages_from(cls, data):
        query = "SELECT * FROM friendships LEFT JOIN messages ON friendships.id=messages.friendship_id LEFT JOIN users ON friendships.friend_id = users.id WHERE friendships.user_id=%(user_id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        friend_message = []
        for message in result:
            data = {
                "id" : message['messages.id'],
                "user_id" : message['user_id'],
                "friend_id" : message['friend_id'],
                "friend_first_name": message['first_name'],
                "friend_last_name" : message['last_name'],
                "content" : message['content'],
                "created_at": message['messages.created_at'],
                "updated_at" : message['messages.updated_at']
            }
            friend_message.append(data)
        return friend_message