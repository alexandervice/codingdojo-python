from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    # call the get all classmethod to get all dojos and ninjas
    # ninjas = Ninja.get_all()
    # dojos = Dojo.get_all_dojos()
    # print(dojos)
    ninjas = Dojo.all_ninjas()
    # print(dojo_ninja)
    return render_template("index.html", ninjas = ninjas, len = len(ninjas))

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
# First we make a data dictionary from our request.form coming from our template.
# The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]
    }
    # We pass the data dictionary into the save method from the Ninja class.
    Ninja.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')
# NOTE never render_template on a POST route

@app.route('/ninjas/add_new')
def add_ninja():
    print("returning to the create a ninja page")
    dojos = Dojo.get_all_dojos()
    return render_template("create_ninja.html", dojos = dojos)

@app.route('/ninjas/<int:ninja_id>')
def show_ninja(ninja_id):
    # calling the get_one method and supplying it with the id of the ninja we want to get
    dojo=Dojo.get_one_ninja(ninja_id)
    ninja=Ninja.get_one_ninja(ninja_id)
    print(ninja)
    return render_template("show_ninja.html",ninja=ninja, dojo=dojo)

@app.route('/ninjas/edit/<int:ninja_id>')
def edit_ninja(ninja_id):
    ninja=Ninja.get_one(ninja_id)
    dojo=Dojo.get_one_ninja(ninja_id)
    dojos = Dojo.get_all_dojos()
    return render_template("edit_ninja.html",ninja=ninja, dojo=dojo, dojos=dojos)

@app.route('/ninjas/update',methods=['POST'])
def update_ninja():
    print(request.form)
    Ninja.update(request.form)
    return redirect('/')

@app.route('/ninjas/delete/<int:ninja_id>')
def delete_ninja(ninja_id):
    Ninja.delete(ninja_id)
    return redirect('/')