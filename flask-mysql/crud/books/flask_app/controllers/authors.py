from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/authors')
def author_page():
    # call the get all classmethod to get all dojos and ninjas
    authors = Author.get_all()
    # print(all_users[0].first_name)
    return render_template("authors.html", authors = authors)

@app.route('/create_author', methods=["POST"])
def create_author():
# First we make a data dictionary from our request.form coming from our template.
# The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name": request.form["name"],
    }
    # We pass the data dictionary into the save method from the class.
    Author.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/authors')
# NOTE never render_template on a POST route

@app.route('/authors/<int:author_id>')
def show_author(author_id):
    # calling the get_one method and supplying it with the id we want to get
    author=Author.get_author_with_books(author_id)
    books = Book.get_all()
    book_ids = []
    fav_ids = []
    unfav_ids = []
    for book in books:
        book_ids.append(book.id)
    for book in author.books:
        fav_ids.append(book.id)
    for id in book_ids:
        if id not in fav_ids:
            unfav_ids.append(id)
    return render_template("show_author.html",author=author, books=books, book_ids=book_ids, unfav_ids=unfav_ids)

# @app.route('/dojos/edit/<int:dojo_id>')
# def edit_dojo(dojo_id):
#     dojo=Dojo.get_one(dojo_id)
#     return render_template("edit_dojo.html",dojo=dojo)

@app.route('/authors/update',methods=['POST'])
def create_favorite():
    id = {
        "author_id": request.form["author_id"],
    }
    # print(request.form)
    Author.favorite(request.form)
    return redirect(f'/authors/{request.form["author_id"]}')

# @app.route('/dojos/delete/<int:dojo_id>')
# def delete_ninja(dojo_id):
#     Dojo.delete(dojo_id)
#     return redirect('/')