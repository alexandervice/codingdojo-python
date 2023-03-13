# Import Flask to allow us to create our app
# render_template is for getting an html page
from flask import Flask, render_template


app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html", rows=8, columns=8, color1="red", color2="black")


@app.route("/test")
def success():
    return "It works"

@app.route('/<int:num1>') 
def rows(num1):
    print(num1)
    return render_template("index.html", rows=num1, columns=8, color1="red", color2="black")

@app.route('/<int:num1>/<int:num2>') 
def columns(num1, num2):
    print(num1, num2)
    return render_template("index.html", rows=num1, columns=num2, color1="red", color2="black")

@app.route('/<int:num1>/<int:num2>/<string:color1>') 
def color1(num1, num2, color1):
    print(num1, num2, color1)
    return render_template("index.html", rows=num1, columns=num2, color1=color1, color2="black")

@app.route('/<int:num1>/<int:num2>/<string:color1>/<string:color2>') 
def color2(num1, num2, color1, color2):
    print(num1, num2, color1, color2)
    return render_template("index.html", rows=num1, columns=num2, color1=color1, color2=color2)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

