# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    database = "books"
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO books (title , num_of_pages , created_at, updated_at ) VALUES (%(title)s, %(num_of_pages)s , NOW() , NOW() );"
        result = connectToMySQL(cls.database).query_db( query, data )
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.database).query_db(query)
        books = []
        # Iterate over the db results and create instances of books with cls.
        for book in results:
            books.append( cls(book) )
        return books

    @classmethod
    def get_one(cls, book_id):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        data = {
            "id": book_id
        }
        results = connectToMySQL(cls.database).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_book_with_authors( cls , book_id ):
        data = {
            "id": book_id
        }
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL(cls.database).query_db( query , data )
        # results will be a list of topping objects with the burger attached to each row. 
        book = cls( results[0] )
        for row_from_db in results:
            # Now we parse the topping data to make instances of toppings and add them into our list.
            author_data = {
                "id" : row_from_db["authors.id"],
                "name" : row_from_db["name"],
                "created_at" : row_from_db["authors.created_at"],
                "updated_at" : row_from_db["authors.updated_at"]
            }
            book.authors.append( author.Author( author_data ) )
        return book

    @classmethod
    def favorite( cls , data ):
        query = "INSERT INTO favorites ( author_id , book_id ) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL(cls.database).query_db( query, data)
    
    
    # @classmethod
    # def get_one_ninja(cls, ninja_id):
    #     query = "SELECT * FROM ninjas LEFT JOIN dojos ON dojos.id = ninjas.dojo_id WHERE ninjas.id = %(id)s;"
    #     data = {
    #         "id": ninja_id
    #     }
    #     results = connectToMySQL(cls.database).query_db(query, data)
    #     return cls(results[0])

    #     # class method to update our ninjas in the database
    # # UPDATE (CRUD)
    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, dojo_id = %(dojo_id)s, updated_at = NOW() WHERE id = %(id)s;"
    #     results = connectToMySQL(cls.database).query_db(query, data)
    #     return results

    # # class method to delete our users in the database
    # # DELETE (CRUD)
    # @classmethod
    # def delete(cls, ninja_id):
    #     query  = "DELETE FROM ninjas WHERE id = %(id)s;"
    #     data = {"id": ninja_id}
    #     results = connectToMySQL(cls.database).query_db(query, data)
    #     return results