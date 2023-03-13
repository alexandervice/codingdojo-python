from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/books')
def book_page():
    books = Book.get_all()
    return render_template("books.html", books=books)

@app.route('/create_book', methods=["POST"])
def create_book():
# First we make a data dictionary from our request.form coming from our template.
# The keys in data need to line up exactly with the variables in our query string.
    data = {
        "title": request.form["title"],
        "num_of_pages" : request.form["num_of_pages"],
    }
    # We pass the data dictionary into the save method from the class.
    Book.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/books')
# NOTE never render_template on a POST route


@app.route('/books/<int:book_id>')
def show_book(book_id):
    # calling the get_one method and supplying it with the id we want to get
    book=Book.get_book_with_authors(book_id)
    authors=Author.get_all()
    author_ids = []
    fav_ids = []
    unfav_ids = []
    for author in authors:
        author_ids.append(author.id)
    for author in book.authors:
        fav_ids.append(author.id)
    for id in author_ids:
        if id not in fav_ids:
            unfav_ids.append(id)
    for i in unfav_ids:
        print(i)
    return render_template("show_book.html",book=book, authors=authors, unfav_ids=unfav_ids)


@app.route('/books/update',methods=['POST'])
def create_favorite_2():
    id = {
        "book_id": request.form["book_id"],
    }
    # print(request.form)
    Book.favorite(request.form)
    return redirect(f'/books/{request.form["book_id"]}')

# @app.route('/ninjas/add_new')
# def add_ninja():
#     print("returning to the create a ninja page")
#     dojos = Dojo.get_all_dojos()
#     return render_template("create_ninja.html", dojos = dojos)

# @app.route('/ninjas/edit/<int:ninja_id>')
# def edit_ninja(ninja_id):
#     ninja=Ninja.get_one(ninja_id)
#     dojo=Dojo.get_one_ninja(ninja_id)
#     dojos = Dojo.get_all_dojos()
#     return render_template("edit_ninja.html",ninja=ninja, dojo=dojo, dojos=dojos)

# @app.route('/ninjas/update',methods=['POST'])
# def update_ninja():
#     print(request.form)
#     Ninja.update(request.form)
#     return redirect('/')

# @app.route('/ninjas/delete/<int:ninja_id>')
# def delete_ninja(ninja_id):
#     Ninja.delete(ninja_id)
#     return redirect('/')