from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/friendships')

@app.route('/friendships')
def book_page():
    users = User.get_all()
    friends = User.get_friendships()
    # print(friends[0][0].first_name)
    friend_data = User.friendship_data()
    
    return render_template("index.html", users=users, friends=friends, friend_data=friend_data)

@app.route('/create_user', methods=["POST"])
def create_user():
# First we make a data dictionary from our request.form coming from our template.
# The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
    }
    # We pass the data dictionary into the save method from the class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/friendships')
# NOTE never render_template on a POST route

@app.route('/friends/update',methods=['POST'])
def create_favorite():
    data = {
        "user_id": request.form["user_id"],
        "friend_id": request.form["friend_id"]
    }
    # print(request.form)
    User.favorite(data)
    return redirect('/friendships')