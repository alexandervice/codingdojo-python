from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.order import Order

@app.route('/')
def index():
    return redirect('/orders')

@app.route('/orders')
def order_list():
    session["old_form"] = {
        "customer_name": "",
        "cookie_type" : "",
        "number_of_boxes" : ""
    }
    # call the get all classmethod to get all orders
    orders = Order.get_all()
    return render_template("index.html", orders = orders, len = len(orders))

@app.route('/create_order', methods=["POST"])
def create_order():
# First we make a data dictionary from our request.form coming from our template.
# The keys in data need to line up exactly with the variables in our query string.
    data = {
        "customer_name": request.form["customer_name"],
        "cookie_type" : request.form["cookie_type"],
        "number_of_boxes" : request.form["number_of_boxes"]
    }
    # validation
    if not Order.validate_order(data):
        print("order creation rejected: bad form entry")
        session["old_form"] = data
        # we redirect to the template with the form.
        return redirect('/add_new')
    print("Saving this data to the database")
    Order.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')
# NOTE never render_template on a POST route

@app.route('/add_new')
def add():
    return render_template("create_order.html")

@app.route('/orders/<int:order_id>')
def show(order_id):
    # calling the get_one method and supplying it with the id of the order we want to get
    order=Order.get_one(order_id)
    return render_template("show_order.html",order=order)

@app.route('/orders/edit/<int:order_id>')
def edit(order_id):
    order=Order.get_one(order_id)
    return render_template("edit_order.html",order=order)

@app.route('/orders/update',methods=['POST'])
def update():
    data = {
        "customer_name": request.form["customer_name"],
        "cookie_type" : request.form["cookie_type"],
        "number_of_boxes" : request.form["number_of_boxes"],
        "order_id": request.form["id"]
    }
    if not Order.validate_order(data):
        print("order creation rejected: bad form entry")
        session["old_form"] = data
        # we redirect to the template with the form.
        return redirect(f'/orders/edit/{data["order_id"]}')
    Order.update(request.form)
    return redirect('/')

@app.route('/orders/delete/<int:order_id>')
def delete(order_id):
    Order.delete(order_id)
    return redirect('/')