from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipie import Recipie

@app.route('/create_recipie', methods=["POST"])
def create_recipie():
    data = {
        "chef_id": session['logged_in_user']["user_id"],
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "date_made" : request.form["date_made"],
        "is_short" : request.form["is_short"]
    }
    if not Recipie.validate_recipie(data):
        print("recipie creation rejected: bad form entry")
        return redirect('/add_new_recipie')
    Recipie.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/recipie_page')
# NOTE never render_template on a POST route

@app.route('/recipies/delete/<int:recipie_id>')
def delete_recipie(recipie_id):
    Recipie.delete(recipie_id)
    return redirect('/recipie_page')


@app.route('/add_new_recipie')
def add_recipie():
    user=User.get_one(session['logged_in_user']["user_id"])
    return render_template("create_recipie.html", user=user)

@app.route('/recipies/<int:recipie_id>')
def show_recipie(recipie_id):
    user=User.get_one(session['logged_in_user']["user_id"])
    # calling the get_one method and supplying it with the id of the recipie we want to get
    recipie=Recipie.get_one(recipie_id)
    recipies=Recipie.get_all_recipies_with_chef()
    for recipie in recipies:
        if recipie.id == recipie_id:
            recipie_with_chef = recipie
            # print(recipie_with_chef.chef)
    return render_template("show_recipie.html",user=user, recipie=recipie_with_chef)

@app.route('/recipies/edit/<int:recipie_id>')
def edit_recipie(recipie_id):
    user=User.get_one(session['logged_in_user']["user_id"])
    recipie=Recipie.get_one(recipie_id)
    return render_template("edit_recipie.html", user=user, recipie=recipie)

@app.route('/recipies/update',methods=['POST'])
def update_recipie():
    data = {
        "chef_id": session['logged_in_user']["user_id"],
        "id": request.form["recipie_id"],
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "date_made" : request.form["date_made"],
        "is_short" : request.form["is_short"]
    }
    if not Recipie.validate_recipie(data):
        print("recipe creation rejected: bad form entry")
        return redirect(f'/recipies/edit/{data["id"]}')
    Recipie.update(data)
    return redirect('/recipie_page')
