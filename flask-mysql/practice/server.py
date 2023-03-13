from flask import Flask, render_template, request, redirect, session

from friend import Friend
# import the class from friend.py

app = Flask(__name__)
app.secret_key = 'verysecretcode'
# set a secret key for security purposes

@app.route('/')
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends[0].first_name)
    return render_template("index.html", friends = friends, len = len(friends))

@app.route('/create_friend', methods=["POST"])
def create_friend():
# First we make a data dictionary from our request.form coming from our template.
# The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')
# NOTE never render_template on a POST route

@app.route('/friend/<int:friend_id>')
def show(friend_id):
    # calling the get_one method and supplying it with the id of the friend we want to get
    friend=Friend.get_one(friend_id)
    return render_template("show_friend.html",friend=friend)

@app.route('/friends/update',methods=['POST'])
def update():
    Friend.update(request.form)
    return redirect('/')

@app.route('/friends/delete/<int:friend_id>')
def delete(friend_id):
    Friend.delete(friend_id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)