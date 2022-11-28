from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema_jg').query_db(query)
        users = []
        for x in results:
            users.append( cls(x) )
        return users

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL('users_schema_jg').query_db( query, data )

    @classmethod
    def delete_all(cls, data):
        query = "DELETE FROM users;"
        return connectToMySQL('users_schema_jg').query_db(query, data)

    @classmethod
    def getUser(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('users_schema_jg').query_db(query,data)
        return cls(result[0])

    @classmethod
    def updateUser(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id= %(id)s;"
        return connectToMySQL('users_schema_jg').query_db(query,data)

    @classmethod
    def destroyUser(cls, data):
        query = "DELETE FROM users where id=%(id)s;"
        return connectToMySQL('users_schema_jg').query_db(query,data)

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user["first_name"]) <=3:
            flash("First name must be at least 3 characters long!", 'error')
            is_valid = False
        if len(user["last_name"]) <=3:
            flash("Last name must be at least 3 characters long!", 'error')
            is_valid = False
        if len(user["email"]) <=3:
            flash("Email must be at least characters long!", 'email')
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash("Invalid email address", 'email')
            is_valid = False
        return is_valid



