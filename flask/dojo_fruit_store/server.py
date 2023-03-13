from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    total = int(request.form["strawberry"])+int(request.form["raspberry"])+int(request.form["apple"])
    now = datetime.now()
    full_name = request.form["first_name"] +" " + request.form["last_name"]
    time = now.strftime("%A, %B %d %Y, at %H:%M:%S %p")
    print(f"Charging {full_name} for {total} fruits.")
    return render_template("checkout.html", total=total, time=time)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    