from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    database = "books"
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # We create a list so that later we can add in all the books that are favorited by this author
        self.books = []
    
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO authors ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL(cls.database).query_db( query, data)
    
    @classmethod
    def get_one(cls, author_id):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        data = {
            "id": author_id
        }
        results = connectToMySQL(cls.database).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(cls.database).query_db(query)
        # Create an empty list to append our instances of ninjas
        all_authors = []
        # Iterate over the db results and create instances of ninjas with cls.
        for author in results:
            all_authors.append( cls(author) )
        return all_authors

    @classmethod
    def get_author_with_books( cls, author_id ):
        data = {
            "id": author_id
        }
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books on favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL(cls.database).query_db( query, data )
        author = cls( results[0] )
        for row_from_db in results:
            
            book_data = {
                "id" : row_from_db["books.id"],
                "title" : row_from_db["title"],
                "num_of_pages" : row_from_db["num_of_pages"],
                "created_at" : row_from_db["books.created_at"],
                "updated_at" : row_from_db["books.updated_at"]
            }
            author.books.append( book.Book( book_data ) )
            # ninjas.append( ninja_data )
        # print(author.books)
        return author
    
    @classmethod
    def favorite( cls , data ):
        query = "INSERT INTO favorites ( author_id , book_id ) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL(cls.database).query_db( query, data)
    
    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE favorites SET author_id = %(author_id)s, book_id = %(book_id)s updated_at = NOW() WHERE id = %(id)s;"
    #     results = connectToMySQL(cls.database).query_db(query, data)
    #     return results
    
    # @classmethod
    # def get_dojo_with_ninjas( cls , dojo_id ):
    #     query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
    #     data = {
    #         "id": dojo_id
    #     }
    #     results = connectToMySQL(cls.database).query_db( query , data )
        
    #     dojo = cls( results[0] )
    #     for row_from_db in results:
            
    #         ninja_data = {
    #             "id" : row_from_db["ninjas.id"],
    #             "first_name" : row_from_db["first_name"],
    #             "last_name" : row_from_db["last_name"],
    #             "age" : row_from_db["age"],
    #             "created_at" : row_from_db["ninjas.created_at"],
    #             "updated_at" : row_from_db["ninjas.updated_at"]
    #         }
    #         dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        
    #     return dojo
    
    # @classmethod
    # def get_one_book(cls, ninja_id):
    #     query = "SELECT * FROM ninjas LEFT JOIN dojos ON dojos.id = ninjas.dojo_id WHERE ninjas.id = %(id)s;"
    #     data = {
    #         "id": ninja_id
    #     }
    #     results = connectToMySQL(cls.database).query_db(query, data)
    #     return cls(results[0])
    
