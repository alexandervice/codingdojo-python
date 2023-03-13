from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app import app
from flask import flash

class Recipie:
    database = "recipies"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.is_short = data['is_short']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # None can represent a currently empty space for a single User dictionary to be placed here, as a Post is made by ONE User. We want a User instance and all their attributes to be placed here, so something like data['...'] will not work as we have to make the User instance ourselves.
        self.chef = None

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO recipies (chef_id, name, description, instructions, date_made, is_short , created_at , updated_at ) VALUES ( %(chef_id)s, %(name)s, %(description)s, %(instructions)s, %(date_made)s, %(is_short)s , NOW() , NOW() );"
        result = connectToMySQL(cls.database).query_db( query, data )
        return result

    @classmethod
    def delete(cls, recipie_id):
        query  = "DELETE FROM recipies WHERE id = %(id)s;"
        data = {"id": recipie_id}
        results = connectToMySQL(cls.database).query_db(query, data)
        return results

    @classmethod
    def get_one(cls, recipie_id):
        query = "SELECT * FROM recipies WHERE id = %(id)s;"
        data = {
            "id": recipie_id
        }
        results = connectToMySQL(cls.database).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE recipies SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, is_short = %(is_short)s, updated_at = NOW() WHERE id = %(id)s;"
        results = connectToMySQL(cls.database).query_db(query, data)
        return results

    @classmethod
    def get_all_recipies_with_chef(cls):
        # Get all posts, and their one associated User that created it
        query = "SELECT * FROM recipies LEFT JOIN users ON recipies.chef_id = users.id;"
        results = connectToMySQL(cls.database).query_db(query)
        all_recipies = []
        for row in results:
            # Create a post class instance from the information from each db row
            one_recipie = cls(row)
            # Prepare to make a User class instance, looking at the class in models/user.py
            one_recipie_chef_info = {
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
            chef = user.User(one_recipie_chef_info)
            # Associate the post class instance with the User class instance by filling in the empty creator attribute in the post class
            one_recipie.chef = chef
            # Append the post containing the associated User to your list of posts
            all_recipies.append(one_recipie)
        return all_recipies
    
    @staticmethod
    def validate_recipie( recipie ):
        is_valid = True
        # test whether a field matches the pattern
        if len(recipie['name']) < 3:
            flash("Name must be at least 3 characters.", "recipie")
            is_valid = False
        elif len(recipie['name']) > 255:
            flash("Name must be less than 256 characters.", "recipie")
            is_valid = False
        if len(recipie['description']) < 3:
            flash("Description must be at least 3 characters.", "recipie")
            is_valid = False
        elif len(recipie['description']) > 255:
            flash("Description must be less than 256 characters.", "recipie")
            is_valid = False
        if len(recipie['instructions']) < 3:
            flash("Instructions must be at least 3 characters.", "recipie")
            is_valid = False
        if len(recipie['date_made']) < 1:
            flash("Date Made field is required.", "recipie")
            is_valid = False
        if len(recipie['is_short']) < 1:
            flash("Under 30 Min must be answered.", "recipie")
            is_valid = False
        return is_valid