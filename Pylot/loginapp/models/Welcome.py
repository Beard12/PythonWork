""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class Welcome(Model):
    def __init__(self):
        super(Welcome, self).__init__()


    def create_user(self,info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # Some basic validation
        if not info['first_name'] or not info['last_name']:
            errors.append('Your first and last name cannot be blank')
        elif len(info['first_name']) < 2 or len(info['last_name']) < 2:
            errors.append('Your first and last name must be at least 2 characters long')
        elif not info['first_name'].isalpha() or info['last_name'].isalpha():
            errors.append('Every character in your first and last name need to be letters')
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['password']:
            errors.append('Your password cannot be blank')
        elif len(info['password']) < 8:
            errors.append('Your password must be at least 8 characters long')
        elif info['password'] != info['cf_password']:
            errors.append('Your password and confirmation must match!')
 
        if errors:
            return {"status": False, "errors": errors}
        else:
            hashed_pw = self.bcrypt.generate_password_hash(info['password'])
            data = {
                'first_name' : info['first_name'],
                'last_name' : info['last_name'],
                'email' : info['email'],
                'password' : hashed_pw,
                'description' : ' ',
                'active' : True,
                'user_level' : admin

            }
            query = "INSERT INTO users (first_name, last_name, email, password) VALUES(:first_name, :last_name, :email, :password)"
            self.db.query_db(query,data)
            return { "status": True}
    def login(self,info):
        errors=[]
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = { 'email': info['email'] }
        user = self.db.query_db(query, data) 

        if len(user) < 1:
            errors.append("We do not have your email on file please register")
            return  {'status': False, "errors" : errors}
        elif self.bcrypt.check_password_hash(user[0]['password'], info['password']):
            return {'status' : True, 'name': user[0]['first_name']}
        else:
            errors.append("We're are sorry but your password did not match our records please try again.")
            return{'status' : False , "errors" : errors }
        


    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """