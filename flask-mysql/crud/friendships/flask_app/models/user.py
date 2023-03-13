# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import friend

class User:
    database = "friendships"
    friends = []
    friendships = []
    friend_combo = []
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.my_friends = []
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users (first_name , last_name , created_at, updated_at ) VALUES (%(first_name)s, %(last_name)s , NOW() , NOW() );"
        result = connectToMySQL(cls.database).query_db( query, data )
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.database).query_db(query)
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
    
    
    @classmethod
    def favorite( cls , data ):
        query = "INSERT IGNORE INTO friendships ( user_id , friend_id, created_at, updated_at ) VALUES (%(user_id)s, %(friend_id)s, NOW() , NOW() );"
        if cls.already_friends(int(data["user_id"]),int(data["friend_id"]), cls.friends):
            return
        print("adding friends")
        cls.friends.append(data)
        return connectToMySQL(cls.database).query_db( query, data)
    
    @classmethod
    def friendship_data( cls ):
        return cls.friends
    
    @classmethod
    def get_friendships( cls ):
        query = "SELECT * FROM friendships LEFT JOIN users as friend_1 on friend_1.id = friendships.user_id LEFT JOIN users as friend_2 on friend_2.id = friendships.friend_id;"
        results = connectToMySQL(cls.database).query_db( query )
        # print("_________________________________________________________")
        # print(results)
        cls.friendships = []
        cls.friends = []
        friend_query = cls( results[0] )
        for row_from_db in results:
            friend_1_data = {
                "id" : row_from_db["friend_1.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "created_at" : row_from_db["friend_1.created_at"],
                "updated_at" : row_from_db["friend_1.updated_at"]
            }
            friend_2_data = {
                "id" : row_from_db["friend_2.id"],
                "first_name" : row_from_db["friend_2.first_name"],
                "last_name" : row_from_db["friend_2.last_name"],
                "created_at" : row_from_db["friend_2.created_at"],
                "updated_at" : row_from_db["friend_2.updated_at"]
            }
            friends = [friend_1_data, friend_2_data]
            id_combo = [int(friend_1_data["id"]), int(friend_2_data["id"])]
            friend_query.friendships.append( friends )
            friend_query.friends.append( id_combo )
        # print(cls.friendships)
        # print(cls.friends)
        return cls.friendships

    @staticmethod
    def already_friends(user_id, friend_id, list):

        if [user_id, friend_id] in list:
            print("these users are already friends")
            return True
        elif[friend_id, user_id] in list:
            print("these users are already friends")
            return True
        elif user_id == friend_id:
            print("these users are the same person")
            return True
        else:
            return False


    @classmethod
    def get_user_and_friend( cls , user_id ):
        data = {
            "id": user_id
        }
        
        query = "SELECT * FROM friendships LEFT JOIN users as friend_1 on friend_1.id = friendships.user_id LEFT JOIN users as friend_2 on friend_2.id = friendships.friend_id WHERE friend_1.id = %(id)s;"
        results = connectToMySQL(cls.database).query_db( query , data )
        friend_query = cls( results[0] )
        for row_from_db in results:
            friend = {
                "id" : row_from_db["friend_2.id"],
                "first_name" : row_from_db["friend_2.first_name"],
                "last_name" : row_from_db["friend_2.last_name"],
                "created_at" : row_from_db["friend_2.created_at"],
                "updated_at" : row_from_db["friend_2.updated_at"]
            }
            friend_query.my_friends.append( friend )
        # print(cls.friendships)
        # print(friend_query)
        return friend_query
    