# Import Flask to allow us to create our app
from flask import Flask  
# Create a new instance of the Flask class called "app"
app = Flask(__name__)    


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  
    # Return the string 'Hello World!' as a response

@app.route("/dojo")
def success():
    return "Dojo!"


# for a route '/say/____' anything after '/say/' gets passed as a variable 'name'
@app.route('/say/<string:name>') 
def hello(name):
    print(name)
    return f"Hi, {name.title()}!"

#  in @app.route('/hello/<name>') the <name> part is always a string SO we can use @app.route('/hello/<int:name>') to have it be a number we can do math with


@app.route('/repeat/<int:number>/<string:word>') 
def repeat(number, word):
    print(number)
    print(word)
    return number*word

@app.route("/<error>")
def nothing_to_see_here(error):
    print(error)
    return "Sorry! No response. Try again."

# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

