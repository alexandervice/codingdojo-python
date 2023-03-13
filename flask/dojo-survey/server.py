from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = 'secretpassword'
# set a secret key for security purposes
# our index route will handle rendering our form

@app.route('/')
def index():
    print("hi")
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    if len(request.form) <4:
        return redirect("/")
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    if 'hotdog' in request.form:
        session["hotdog"] = "Yes"
    else:
        session["hotdog"] = "No"
    return redirect("/results")

@app.route('/results')
def results():
    print("here is the stuff")
    return render_template("results.html")

# uneccessary code below

# @app.route('/')
# def index():
#     if 'number' in session:
#         print(f'the secret number is: {session["number"]}')
#     else:
#         session["number"] = random.randint(1, 100)
#         print(f'the secret number has been set to: {session["number"]}')
#     if 'guess' in session:
#         print(f'your guess was: {session["guess"]}')
#         if int(session["guess"]) == session["number"]:
#             print("you did it!")
#             return render_template("win.html")
#         elif int(session["guesses"]) > 5:
#             return render_template("lose.html")
#         elif int(session["guess"]) > session["number"]:
#             print("Too high!")
#             return render_template("high.html")
#         elif int(session["guess"]) < session["number"]:
#             print("Too low!")
#             return render_template("low.html")
#         else:
#             print("error")
#     return render_template("index.html")

# @app.route('/guess', methods=['POST'])
# def guess():
#     if 'guesses' in session:
#         session["guesses"] += 1
#         print(f'You have made: {session["guesses"]} guesses')
#     else:
#         print("This was your first guess")
#         session["guesses"] = 1
#     session["guess"] = request.form["guess"]
#     return redirect("/")

# @app.route('/restart', methods=['POST'])
# def reset():
#     print("Resetting Session")
#     session.pop("number")
#     session.pop("guess")
#     session.pop("guesses")
#     return redirect("/")

# @app.route('/leaderboard', methods=['POST'])
# def leaderboard():
#     print("List of all the winners")
#     if 'winners' in session:
#         session["winners"] += 1
#     else:
#         print("First Winner")
#         session["winners"] = 0
#         session["leaderboard"] = []
#     winner = {}
#     winner["name"] = request.form["name"]
#     winner["guesses"] = session["guesses"]
#     print(winner)
#     session["leaderboard"].append(winner)
#     return redirect("/winners")

# @app.route('/winners')
# def winners():
#     print("Here are all the winners!")
#     return render_template("leaderboard.html")


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