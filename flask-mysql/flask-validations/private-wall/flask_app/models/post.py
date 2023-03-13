from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, comment
from flask_app import app
from flask import flash

class Post:
    database = "private-wall"
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # None can represent a currently empty space for a single User dictionary to be placed here, as a Post is made by ONE User. We want a User instance and all their attributes to be placed here, so something like data['...'] will not work as we have to make the User instance ourselves.
        self.creator = None
        # add a spot for all the comments on each post
        self.comments = []

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO posts (user_id, content , created_at , updated_at ) VALUES ( %(user_id)s, %(content)s , NOW() , NOW() );"
        result = connectToMySQL(cls.database).query_db( query, data )
        return result
    
    @classmethod
    def foreign_key_on(cls):
        return connectToMySQL(cls.database).query_db("SET FOREIGN_KEY_CHECKS=1;")
    
    @classmethod
    def foreign_key_off(cls):
        return connectToMySQL(cls.database).query_db("SET FOREIGN_KEY_CHECKS=0;")

    @classmethod
    def delete(cls, post_id):
        # connectToMySQL(cls.database).query_db("SET FOREIGN_KEY_CHECKS=0;")
        query  = "DELETE FROM posts WHERE id = %(id)s;"
        data = {"id": post_id}
        results = connectToMySQL(cls.database).query_db(query, data)
        # connectToMySQL(cls.database).query_db("SET FOREIGN_KEY_CHECKS=1;")
        return results

    @classmethod
    def get_all_posts_with_creator(cls):
        # Get all posts, and their one associated User that created it
        query = "SELECT * FROM posts LEFT JOIN users ON posts.user_id = users.id;"
        results = connectToMySQL(cls.database).query_db(query)
        all_posts = []
        for row in results:
            # Create a post class instance from the information from each db row
            one_post = cls(row)
            # Prepare to make a User class instance, looking at the class in models/user.py
            one_posts_author_info = {
                # Any fields that are used in BOTH tables will have their name changed, which depends on the order you put them in the JOIN query, use a print statement in your classmethod to show this.
                "id": row['users.id'], 
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "handle": row['handle'],
                "password": row['password'],
                "birth_date": row["birth_date"],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            # Create the User class instance that's in the user.py model file
            author = user.User(one_posts_author_info)
            # Associate the post class instance with the User class instance by filling in the empty creator attribute in the post class
            one_post.creator = author
            # Append the post containing the associated User to your list of posts
            all_posts.append(one_post)
        return all_posts
    
    @staticmethod
    def validate_post( post ):
        is_valid = True
        # test whether a field matches the pattern
        if len(post['content']) < 1:
            flash("Post content must not be blank.", "post")
            is_valid = False
        return is_valid