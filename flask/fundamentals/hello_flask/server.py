# Import Flask to allow us to create our app
# render_template is for getting an html page
from flask import Flask, render_template


app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html", phrase="hello", times=5)
    # This opens our html file.
    # it must be saved in a folder called "templates"
    # 2 new arguments with names (phrase) and (times)
    # this will let us use logic in the html
    # old - return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route("/success")
def success():
    return "Success"

@app.route('/hello/<string:phrase>/<int:number>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(phrase,number):
    print(phrase, number)
    return render_template("hello.html", phrase=phrase, number=number)

#  in @app.route('/hello/<name>') the <name> part is always a string SO we can use @app.route('/hello/<int:name>') to have it be a number we can do math with

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

