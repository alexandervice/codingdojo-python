from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, post, comment
from flask_app import app
from datetime import date, datetime
from flask import flash

def calculate_age(created_at):
        days_in_year = 365.2425
        days_in_month = 30
        seconds_in_day = 86400
        seconds_in_hour = 3600
        today=date.today()
        now = datetime.now()
        if int((now - created_at).days) > days_in_year:
            age = int((now - created_at).days / days_in_year )
            return f"{age} years(s) ago"
        if int((now - created_at).days) > days_in_month:
            age = int((now - created_at).days / days_in_month )
            return f"{age} month(s) ago"
        if int((now - created_at).seconds) > seconds_in_day:
            age = int((now - created_at).seconds / seconds_in_day )
            return f"{age} days(s) ago"
        if int((now - created_at).seconds) > seconds_in_hour:
            age = int((now - created_at).seconds / seconds_in_hour )
            return f"{age} hours(s) ago"
        age = age = int((now - created_at).seconds / 60 )
        return f"{age} minutes(s) ago"

class Message:
    database = "private-wall"
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # None can represent a currently empty space for a single User dictionary to be placed here, as a Post is made by ONE User. We want a User instance and all their attributes to be placed here, so something like data['...'] will not work as we have to make the User instance ourselves.
        self.sender = None
        # add a spot for all the comments on each post
        self.recipient = None
        # add a spot for age to be displayed as a string
        self.age = None

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO messages (sender_id, recipient_id, content , created_at , updated_at ) VALUES ( %(sender_id)s, %(recipient_id)s, %(content)s , NOW() , NOW() );"
        result = connectToMySQL(cls.database).query_db( query, data )
        return result

    @classmethod
    def delete(cls, message_id):
        query  = "DELETE FROM messages WHERE id = %(id)s;"
        data = {"id": message_id}
        results = connectToMySQL(cls.database).query_db(query, data)
        return results

    @classmethod
    def get_all_messages_for_recipient_with_sender(cls):
        # Get all messages, with the sender and recipient
        query = "SELECT * FROM messages LEFT JOIN users as senders ON messages.sender_id = senders.id LEFT JOIN users as recipients ON messages.recipient_id = recipients.id;"
        results = connectToMySQL(cls.database).query_db(query)
        all_messages = []
        for row in results:
            # Create a message class instance from the information from each db row
            one_message = cls(row)
            # Prepare to make a message class instance
            one_message_sender_info = {
                # Any fields that are used in BOTH tables will have their name changed, which depends on the order you put them in the JOIN query, use a print statement in your classmethod to show this.
                "id": row['senders.id'], 
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "handle": row['handle'],
                "password": row['password'],
                "birth_date": row['birth_date'],
                "created_at": row['senders.created_at'],
                "updated_at": row['senders.updated_at']
            }
            one_message_recipient_info = {
                # Any fields that are used in BOTH tables will have their name changed, which depends on the order you put them in the JOIN query, use a print statement in your classmethod to show this.
                "id": row['recipients.id'], 
                "first_name": row['recipients.first_name'],
                "last_name": row['recipients.last_name'],
                "email": row['recipients.email'],
                "handle": row['recipients.handle'],
                "password": row['recipients.password'],
                "birth_date": row['recipients.birth_date'],
                "created_at": row['recipients.created_at'],
                "updated_at": row['recipients.updated_at']
            }

            # Create the User class instance that's in the user.py model file
            sender = user.User(one_message_sender_info)
            # Associate the message class instance with the User class instance by filling in the empty sender attribute in the message class
            one_message.sender = sender
            
            # Create the User class instance that's in the user.py model file
            recipient = user.User(one_message_recipient_info)
            # Associate the message class instance with the User class instance by filling in the empty sender attribute in the message class
            one_message.recipient = recipient

            # age calculation
            age = calculate_age(row["created_at"])
            one_message.age = age
            # Append the message containing the associated Users to your list of messages
            all_messages.append(one_message)
        return all_messages
    
    @staticmethod
    def validate_message( message ):
        is_valid = True
        # test whether a field matches the pattern
        if len(message['content']) < 5:
            flash("Message must be at least 5 characters.", message["recipient_id"])
            # print(message["recipient_id"])
            is_valid = False
        return is_valid