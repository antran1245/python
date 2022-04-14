# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the dojo table from our database
from flask_app.models.ninja import Ninja

database = 'dojos_and_ninjas_schema'
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(database).query_db(query)
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    # Create a new dojo entry
    @classmethod
    def create_dojo(cls, data ):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL(database).query_db( query, data )

    # Read one row in dojos
    @classmethod
    def read_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(database).query_db(query, data)
    
    # Get all the ninja then create instance of them into a list
    @classmethod
    def get_all_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id=dojos.id WHERE dojos.id=%(id)s;"
        result = connectToMySQL(database).query_db( query, data )
        ninjas = []
        for ninja in result:
            data = {
                "id" : ninja['id'],
                "first_name" : ninja['first_name'],
                "last_name" : ninja['last_name'],
                "age" : ninja['age'],
                "created_at" : ninja['created_at'],
                "updated_at" : ninja['updated_at']
            }
            ninjas.append(Ninja(data))
        return ninjas