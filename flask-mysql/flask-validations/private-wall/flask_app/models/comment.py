from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, post
from flask_app import app
from flask import flash

class Comment:
    database = "private-wall"
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # None can represent a currently empty space for a single User dictionary to be placed here, as a Post is made by ONE User. We want a User instance and all their attributes to be placed here, so something like data['...'] will not work as we have to make the User instance ourselves.
        self.creator = None
        # add a spot for all the comments on each post
        self.post = None

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO comments (user_id, post_id, content , created_at , updated_at ) VALUES ( %(user_id)s, %(post_id)s, %(content)s , NOW() , NOW() );"
        result = connectToMySQL(cls.database).query_db( query, data )
        return result

    @classmethod
    def delete(cls, comment_id):
        query  = "DELETE FROM comments WHERE id = %(id)s;"
        data = {"id": comment_id}
        results = connectToMySQL(cls.database).query_db(query, data)
        return results

    @classmethod
    def get_all_comments_for_post_with_creator(cls):
        # Get all comments, for each post and their one associated User that created it
        query = "SELECT * FROM comments LEFT JOIN users ON comments.user_id = users.id LEFT JOIN posts on comments.post_id = posts.id;"
        results = connectToMySQL(cls.database).query_db(query)
        all_comments = []
        for row in results:
            # Create a comment class instance from the information from each db row
            one_comment = cls(row)
            # Prepare to make a User class instance, looking at the class in models/user.py
            one_comment_author_info = {
                # Any fields that are used in BOTH tables will have their name changed, which depends on the order you put them in the JOIN query, use a print statement in your classmethod to show this.
                "id": row['users.id'], 
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "handle": row['handle'],
                "password": row['password'],
                "birth_date": row['birth_date'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            one_comment_post_info = {
                "id": row["posts.id"],
                "content": row["posts.content"],
                "created_at": row['posts.created_at'],
                "updated_at": row['posts.updated_at']
            }

            # Create the User class instance that's in the user.py model file
            author = user.User(one_comment_author_info)
            # Associate the post class instance with the User class instance by filling in the empty creator attribute in the comment class
            one_comment.creator = author
            
            # Create the Post class instance that is in the post.py model file
            message = post.Post(one_comment_post_info)
            one_comment.post = message

            # Append the post containing the associated User to your list of posts
            all_comments.append(one_comment)
        return all_comments
    
    @staticmethod
    def validate_comment( comment ):
        is_valid = True
        # test whether a field matches the pattern
        if len(comment['content']) < 1:
            flash("Comment cannot be empty.", comment["post_id"])
            print(comment["post_id"])
            is_valid = False
        return is_valid