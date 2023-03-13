# Import Flask to allow us to create our app
# render_template is for getting an html page
from flask import Flask, render_template


app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return "please go to localhost:5000/play"
    return render_template("index.html", phrase="hello", times=5)
    # This opens our html file.
    # it must be saved in a folder called "templates"
    # 2 new arguments with names (phrase) and (times)
    # this will let us use logic in the html
    # old - return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route("/test")
def success():
    return "It works"

@app.route('/play') 
# for a route '/play/____' anything after '/play/' gets passed as a variable 'name'
def play():
    print("heyo")
    return render_template("index.html", number=3, color="aqua")

@app.route('/play/<int:number>') 
# for a route '/play/____' anything after '/play/' gets passed as a variable 'name'
def play_2(number):
    print(number)
    return render_template("index.html", number=number, color="aqua")


@app.route('/play/<int:number>/<string:color>') 
# for a route '/play/____' anything after '/play/' gets passed as a variable 'name'
def play_3(number, color):
    print(number, color)
    return render_template("index.html", number=number, color=color)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

