# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database

class User:
    database = "users"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        result = connectToMySQL(cls.database).query_db( query, data )
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.database).query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_one(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {
            "id": user_id
        }
        results = connectToMySQL(cls.database).query_db(query, data)
        return cls(results[0])

# class Friend:
#     database = "first_flask"
#     # call with cls.database
#     def __init__( self , data ):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.occupation = data['occupation']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
#     # Now we use class methods to query our database

#     # class method to save our friend to the database
#     # Create (CRUD)
#     @classmethod
#     def save(cls, data ):
#         query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
#         # data is a dictionary that will be passed into the save method from server.py
#         result = connectToMySQL(cls.database).query_db( query, data )
#         return result

#     # class method to view our friends in the database
#     # Read (CRUD)
#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM friends;"
#         # make sure to call the connectToMySQL function with the schema you are targeting.
#         results = connectToMySQL(cls.database).query_db(query)
#         # Create an empty list to append our instances of friends
#         friends = []
#         # Iterate over the db results and create instances of friends with cls.
#         for friend in results:
#             friends.append( cls(friend) )
#         return friends
            
#     @classmethod
#     def get_one(cls, friend_id):
#         query = "SELECT * FROM friends WHERE id = %(id)s;"
#         # make sure to call the connectToMySQL function with the schema you are targeting.
#         data = {
#             "id": friend_id
#         }
#         results = connectToMySQL(cls.database).query_db(query, data)
#         return cls(results[0])