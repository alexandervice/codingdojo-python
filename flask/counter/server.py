from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# set a secret key for security purposes
# our index route will handle rendering our form
@app.route('/')
def index():
    if 'count' in session:
        session["count"] += 1
        print(f'the count is: {session["count"]}')
    else:
        print("The count has been reset to 1")
        session["count"] = 1
    if 'visits' in session:
        session["visits"] += 1
        print(f'You have visited the page {session["visits"]} times.')
    else:
        print("This is your first time visiting the page")
        session["visits"] = 1
    return render_template("index.html")

@app.route('/count', methods=['POST'])
def count1():
    session["count"] += 1
    return redirect("/")

@app.route('/destroy_session', methods=['POST'])
def reset():
    print("Resetting Count")
    session.pop("count")
    return redirect("/")

@app.route('/counter', methods=['POST'])
def count2():
    print(request.form["counter"])
    if request.form["counter"].isdigit():
        print(f"adding {request.form['counter']} to the count")
        session["count"] += int(request.form["counter"])-1
    else:
        print("invalid input")
        session["count"] -= 1
    return redirect("/")

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     # Here we add two properties to session to store the name and email
#     session["username"] = request.form['name']
#     session["useremail"] = request.form['email']
#     # Never render a template on a POST request.
#     # Instead we will redirect to our index route.
#     return redirect("/show")

# @app.route('/show')
# def show_user():
#     return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

# or

# @app.route('/show')
# def show_user():
#     return render_template('show.html')
# this only works if we have the session info stored in the html template




if __name__ == "__main__":
    app.run(debug=True)

