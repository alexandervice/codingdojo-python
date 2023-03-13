# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

number_of_boxes_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Order:
    database = "cookie_orders"
    def __init__( self , data ):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.number_of_boxes = int(data['number_of_boxes'])
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO orders ( customer_name , cookie_type , number_of_boxes , created_at, updated_at ) VALUES ( %(customer_name)s , %(cookie_type)s , %(number_of_boxes)s , NOW() , NOW() );"
        result = connectToMySQL(cls.database).query_db( query, data )
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders;"
        results = connectToMySQL(cls.database).query_db(query)
        # Create an empty list to append our instances of orders
        orders = []
        for order in results:
            orders.append( cls(order) )
        return orders

    @classmethod
    def get_one(cls, order_id):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        data = {
            "id": order_id
        }
        results = connectToMySQL(cls.database).query_db(query, data)
        return cls(results[0])
    
        # class method to update our orders in the database
    # UPDATE (CRUD)
    @classmethod
    def update(cls, data):
        query = "UPDATE orders SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, number_of_boxes = %(number_of_boxes)s, updated_at = NOW() WHERE id = %(id)s;"
        results = connectToMySQL(cls.database).query_db(query, data)
        return results

    # class method to delete our orders in the database
    # DELETE (CRUD)
    @classmethod
    def delete(cls, order_id):
        query  = "DELETE FROM orders WHERE id = %(id)s;"
        data = {"id": order_id}
        results = connectToMySQL(cls.database).query_db(query, data)
        return results
    
    # Validations
    # @classmethod
    # def check_duplicates(cls, new_order):
    #     query = "SELECT * FROM orders;"
    #     results = connectToMySQL(cls.database).query_db(query)
    #     # Create an empty list to append our instances of orders
    #     orders = []
    #     is_valid = True
    #     for order in results:
    #         orders.append( cls(order) )
    #         # if new_order['customer_name'] == order["customer_name"] and new_order['cookie_type'] == order["cookie_type"]:
    #         #     flash("That order is already in the system!", "duplicate")
    #         #     is_valid = False
    #         if new_order['number_of_boxes'] == order["number_of_boxes"]:
    #             flash("That number_of_boxes is already registered with a order!", "duplicate")
    #             is_valid = False
    #     return is_valid

    # Validations
    @staticmethod
    def validate_order(order ):
        is_valid = True
        # test whether a field matches the pattern
        if len(order['number_of_boxes']) < 1:
            flash("Number of Boxes must be greater than 0.", "number_of_boxes")
            is_valid = False
        if order['number_of_boxes'].isnumeric():
            if int(order['number_of_boxes']) < 1:
                flash("Number of Boxes must be greater than 0.", "number_of_boxes")
                is_valid = False
        if len(order['customer_name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(order['cookie_type']) < 2:
            flash("Cookie Type must be at least 2 characters.")
            is_valid = False
        return is_valid