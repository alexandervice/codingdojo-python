# #  use %()s instead of f-strings due to security issues
# query = "INSERT INTO friends (first_name, last_name, occupation) VALUES ( %(first_name)s, %(last_name)s, %(occupation)s);"

# data = {
#     "first_name": "Brandon",
#     "last_name": "Davis",
#     "occupation": "Software Engineer"
# }
# #  notice the query uses the same terms as our dictionary

# # mysql.query_db(query, data)

# ------------------------------------------------------------------------------- 
# NOTE - SQL Injection - Security NOTE
# query = "SELECT * FROM users WHERE email = %(email)s;"
# data = { 'email' : request.form['email'] }
# result = mysql.query_db(query, data)
# # this is in our friends.py file (inside a classmethod)


# # this code is for demonstration purposes only
# # DO NOT use this code in production, it will leave you vulnerable to SQL injection
# query = f"SELECT * FROM users WHERE email = '{request.form['email']}';"
# result = mysql.query_db(query)
# #  BAD CODE ^

# query = "SELECT * FROM users WHERE email = %(email)s;"

# # the placeholder variable is called email
# # it must match the key name in the data dictionary
# data = { 
# # this 'email' Key in data must be named to match the placeholder in the query.
#     'email' : request.form['email'] 
# }
# result = mysql.query_db(query, data)

# ------------------------------------------------------------------------------- 

