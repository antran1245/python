# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the dojo table from our database
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
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(database).query_db(query)
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    @classmethod
    def create_dojo(cls, data ):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL(database).query_db( query, data )

    @classmethod
    def read_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(dojo_id)s"
        return connectToMySQL(database).query_db(query, data)