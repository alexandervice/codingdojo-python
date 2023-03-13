from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    # print(all_users[0].first_name)
    return render_template("index.html", users = users, len = len(users))

@app.route('/create_user', methods=["POST"])
def create_user():
    print("running this script")
# First we make a data dictionary from our request.form coming from our template.
# The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # validate the email (and other things if we add them to the .validate_user method)
    if not User.validate_user(data):
        print("user creation rejected")
        # we redirect to the template with the form.
        return redirect('create_user.html')
    # We pass the data dictionary into the save method from the User class.
    print(f"Saving this data as a user: {data}")
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')
# NOTE never render_template on a POST route

@app.route('/add_new')
def add():
    return render_template("create_user.html")

@app.route('/users/<int:user_id>')
def show(user_id):
    # calling the get_one method and supplying it with the id of the user we want to get
    user=User.get_one(user_id)
    return render_template("show_user.html",user=user)

@app.route('/users/edit/<int:user_id>')
def edit(user_id):
    user=User.get_one(user_id)
    return render_template("edit_user.html",user=user)

@app.route('/users/update',methods=['POST'])
def update():
    print(request.form)
    User.update(request.form)
    return redirect('/')

@app.route('/users/delete/<int:user_id>')
def delete(user_id):
    User.delete(user_id)
    return redirect('/')