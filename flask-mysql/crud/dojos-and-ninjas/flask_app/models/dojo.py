from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    database = "dojos-ninjas"
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # We create a list so that later we can add in all the ninjas that are associated with a dojo.
        self.ninjas = []
        self.info = []
    
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO dojos ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL(cls.database).query_db( query, data)
    
    @classmethod
    def get_one_dojo(cls, dojo_id):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {
            "id": dojo_id
        }
        results = connectToMySQL(cls.database).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.database).query_db(query)
        # Create an empty list to append our instances of ninjas
        all_dojos = []
        # Iterate over the db results and create instances of ninjas with cls.
        for dojo in results:
            all_dojos.append( cls(dojo) )
        return all_dojos

    @classmethod
    def get_dojo_with_ninjas( cls , dojo_id ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        data = {
            "id": dojo_id
        }
        results = connectToMySQL(cls.database).query_db( query , data )
        
        dojo = cls( results[0] )
        for row_from_db in results:
            
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        
        return dojo
    
    @classmethod
    def get_one_ninja(cls, ninja_id):
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON dojos.id = ninjas.dojo_id WHERE ninjas.id = %(id)s;"
        data = {
            "id": ninja_id
        }
        results = connectToMySQL(cls.database).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def all_ninjas( cls ):
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON dojos.id = ninjas.dojo_id;"
        results = connectToMySQL(cls.database).query_db( query )
        ninjas = []
        # dojo = cls( results[0] )
        for row_from_db in results:
            
            ninja_data = {
                "id" : row_from_db["id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "dojo": row_from_db["name"],
                "dojo_id": row_from_db["dojo_id"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db["updated_at"]
            }
            # dojo.ninjas.append( ninja.Ninja( ninja_data ) )
            ninjas.append( ninja_data )
        # print(ninjas)
        return ninjas
