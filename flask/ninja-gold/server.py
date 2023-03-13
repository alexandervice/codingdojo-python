from flask import Flask, render_template, request, redirect, session
import random               # import the random module
import datetime
random.randint(1, 100)      # random number between 1-100

app = Flask(__name__)
app.secret_key = 'moneybags'
# set a secret key for security purposes
# our index route will handle rendering our form



@app.route('/')
def index():
    if "turns" in session:
        session["turns"] -= 1
        if session["turns"] < 0:
            if session['gold'] < 500:
                game_over = '<form action="/reset" method="post"><button type="submit"  class="btn btn-danger btn-lg mt-1">Start Over</button></form>'
                return render_template("index.html",game_over=game_over, message="REVO-EMAG", len=len(session["message"]))
            else:
                game_over = '<form action="/reset" method="post"><button type="submit"  class="btn btn-success btn-lg mt-1">Start Over</button></form>'
                return render_template("index.html",game_over=game_over, message="REVO-EMAG", len=len(session["message"]))
    else:
        session["turns"] = 15
    if "gold" in session:
        print(f"You have {session['gold']} gold.")
        if "money" in session:
            if session["money"] < 1:
                message = (f"<p class='text-start text-danger'>Entered the Casino and lost {session['money']} gold... Bummer!      ({datetime.datetime.now().strftime('%I:%M:%S %p')})</p>")
                session["message"] += [message]
                print(type(session["message"]))
                print(session["message"])
                return render_template("index.html", message=session["message"], len=len(session["message"]))
            message = (f"<p class='text-start text-success'>Earned {session['money']} gold from the {session['building']}!      ({datetime.datetime.now().strftime('%I:%M:%S %p')})</p>")
            session["message"] += [message]
            print(type(session["message"]))
            print(session["message"])
            return render_template("index.html", message=session["message"], len=len(session["message"]))
        else:
            print("no money")
            session["message"] = []
    else:
        session["gold"] = 0
        session["message"] = []
    print(type(session["message"]))
    return render_template("index.html", message=session["message"], len=len(session["message"]))

@app.route('/process_money', methods=['POST'])
def process():
    explore = {
        "farm": random.randint(10, 20),
        "cave": random.randint(5, 10),
        "house": random.randint(2, 5),
        "casino": random.randint(-50, 50)
    }
    print(request.form["building"])
    if request.form["building"] in explore:
        session['money'] = explore[request.form["building"]]
        session["gold"] += session['money']
        session['building'] = request.form["building"]
    else:
        print("error")
        session['building'] = "somewhere"

    # if request.form["building"] == "farm":
    #     session['money'] = random.randint(10, 20)
    #     session['building'] = "farm"
    #     session["gold"] += session['money']
    # elif request.form["building"] == "cave":
    #     session['money'] = random.randint(5, 10)
    #     session['building'] = "cave"
    #     session["gold"] += session['money']
    # elif request.form["building"] == "house":
    #     session['money'] = random.randint(2, 5)
    #     session['building'] = "house"
    #     session["gold"] += session['money']
    # elif request.form["building"] == "casino":
    #     session['money'] = random.randint(-50,50)
    #     session['building'] = "casino"
    #     session["gold"] += session['money']
    # else:
    #     print("error")
    return redirect("/")

@app.route('/reset', methods=['POST'])
def reset():
    print("Resetting Session")
    session.pop("money")
    session.pop("gold")
    session.pop("building")
    session.pop("message")
    session.pop("turns")
    return redirect("/")



# @app.route('/results')
# def results():
#     print("here is the stuff")
#     return render_template("results.html")





# @app.route('/process', methods=['POST'])
# def process():
#     print(request.form)
#     if len(request.form) <4:
#         return redirect("/")
#     session["name"] = request.form["name"]
#     session["location"] = request.form["location"]
#     session["language"] = request.form["language"]
#     session["comment"] = request.form["comment"]
#     if 'hotdog' in request.form:
#         session["hotdog"] = "Yes"
#     else:
#         session["hotdog"] = "No"
#     return redirect("/results")

# @app.route('/results')
# def results():
#     print("here is the stuff")
#     return render_template("results.html")

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