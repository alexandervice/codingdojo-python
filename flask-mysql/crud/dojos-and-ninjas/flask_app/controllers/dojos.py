from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def dojo_page():
    # call the get all classmethod to get all dojos and ninjas
    dojos = Dojo.get_all_dojos()
    # print(all_users[0].first_name)
    return render_template("dojos.html", dojos = dojos)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
# First we make a data dictionary from our request.form coming from our template.
# The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name": request.form["name"],
    }
    # We pass the data dictionary into the save method from the Dojo class.
    Dojo.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dojos')
# NOTE never render_template on a POST route

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    # calling the get_one method and supplying it with the id of the dojo we want to get
    dojo=Dojo.get_dojo_with_ninjas(dojo_id)
    print(dojo.ninjas)
    return render_template("show_dojo.html",dojo=dojo)

# @app.route('/dojos/edit/<int:dojo_id>')
# def edit_dojo(dojo_id):
#     dojo=Dojo.get_one(dojo_id)
#     return render_template("edit_dojo.html",dojo=dojo)

# @app.route('/dojos/update',methods=['POST'])
# def update_dojo():
#     print(request.form)
#     Dojo.update(request.form)
#     return redirect('/')

# @app.route('/dojos/delete/<int:dojo_id>')
# def delete_ninja(dojo_id):
#     Dojo.delete(dojo_id)
#     return redirect('/')