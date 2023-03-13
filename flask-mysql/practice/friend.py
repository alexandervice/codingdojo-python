# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    database = "first_flask"
    # call with cls.database
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    # class method to save our friend to the database
    # Create (CRUD)
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL(cls.database).query_db( query, data )
        return result

    # class method to view our friends in the database
    # Read (CRUD)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.database).query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends
            
    @classmethod
    def get_one(cls, friend_id):
        query = "SELECT * FROM friends WHERE id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        data = {
            "id": friend_id
        }
        results = connectToMySQL(cls.database).query_db(query, data)
        return cls(results[0])

    # class method to update our friends in the database
    # UPDATE (CRUD)
    @classmethod
    def update(cls, data):
        query = """
                UPDATE friends 
                SET first_name = %(first_name)s, 
                last_name = %(last_name)s, 
                email = %(email)s 
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.database).query_db(query, data)
        return results

    # class method to delete our friends in the database
    # DELETE (CRUD)
    @classmethod
    def delete(cls, friend_id):
        query  = "DELETE FROM friends WHERE id = %(id)s;"
        data = {"id": friend_id}
        results = connectToMySQL(cls.database).query_db(query, data)
        return results