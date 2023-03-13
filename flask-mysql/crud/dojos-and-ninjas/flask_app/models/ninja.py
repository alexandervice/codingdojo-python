# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    database = "dojos-ninjas"
    def __init__( self , data, dojo="Seattle" ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.dojo = dojo
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas (dojo_id, first_name , last_name , age , created_at, updated_at ) VALUES (%(dojo_id)s, %(first_name)s , %(last_name)s , %(age)s , NOW() , NOW() );"
        result = connectToMySQL(cls.database).query_db( query, data )
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.database).query_db(query)
        # Create an empty list to append our instances of ninjas
        ninjas = []
        # Iterate over the db results and create instances of ninjas with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def get_one(cls, ninja_id):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        data = {
            "id": ninja_id
        }
        results = connectToMySQL(cls.database).query_db(query, data)
        return cls(results[0])
    

    @classmethod
    def get_one_ninja(cls, ninja_id):
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON dojos.id = ninjas.dojo_id WHERE ninjas.id = %(id)s;"
        data = {
            "id": ninja_id
        }
        results = connectToMySQL(cls.database).query_db(query, data)
        return cls(results[0])

        # class method to update our ninjas in the database
    # UPDATE (CRUD)
    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, dojo_id = %(dojo_id)s, updated_at = NOW() WHERE id = %(id)s;"
        results = connectToMySQL(cls.database).query_db(query, data)
        return results

    # class method to delete our users in the database
    # DELETE (CRUD)
    @classmethod
    def delete(cls, ninja_id):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        data = {"id": ninja_id}
        results = connectToMySQL(cls.database).query_db(query, data)
        return results