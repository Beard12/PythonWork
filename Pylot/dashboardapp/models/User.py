""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re
from time import strftime, localtime

class User(Model):
    def __init__(self):
        super(User, self).__init__()


    def create_user(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        if not info['first_name'] or not info['last_name']:
            errors.append('Your first and last name cannot be blank')
        elif len(info['first_name']) < 2 or len(info['last_name']) < 2:
            errors.append('Your first and last name must be at least 2 characters long')
        elif not info['first_name'].isalpha() or not info['last_name'].isalpha():
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
                'user_level' : 'admin'

            }
            query = "INSERT INTO users (first_name, last_name, email, password, description, user_level, active, created_at, updated_at) VALUES(:first_name, :last_name, :email, :password, :description, :user_level, :active, NOW(), NOW())"
            self.db.query_db(query,data)
            query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            data = { 'email': info['email'] }
            user = self.db.query_db(query, data)
            if user[0]['user_level'] == 'admin':
                return { "status": True, 'id' : user[0]['id'], 'admin' : True}
            else:
                return { "status": True, 'id' : user[0]['id'], 'admin' : False}


    def login_user(self,info):
        errors=[]
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = { 'email': info['email'] }
        user = self.db.query_db(query, data) 

        if len(user) < 1:
            errors.append("We do not have your email on file please register")
            return  {'status': False, "errors" : errors}
        elif user[0]['active'] == False:
            errors.append("We do not have your email on file please register")
            return  {'status': False, "errors" : errors}
        elif self.bcrypt.check_password_hash(user[0]['password'], info['password']):
            if user[0]['user_level'] == 'admin':
                return { "status": True, 'id' :user[0]['id'], 'admin' : True}
            else:
                return { "status": True, 'id' :user[0]['id'], 'admin' : False}
        else:
            errors.append("We're are sorry but your password did not match our records please try again.")
            return{'status' : False , "errors" : errors }
    def select_all_users(self):
        query ="SELECT * FROM users"
        users = self.db.query_db(query)
        return users

    def select_user(self, id):
        query ="SELECT * FROM users WHERE id = :id"
        data = {'id': id }
        user = self.db.query_db(query, data)
        if len(user) < 1:
            return False
        elif user[0]['active'] == False:
            return False
        else:
            return user[0]
    def changepass(self,info):
        errors= []
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
            query = "UPDATE users SET password = :password, updated_at = NOW() WHERE id = :id"
            data = { 'id' : info['id'],  'password' : hashed_pw }
            self.db.query_db(query,data)
            return {"status" : True }

    def changename(self,info):
        errors= []
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        if not info['first_name'] or not info['last_name']:
            errors.append('Your first and last name cannot be blank')
        elif len(info['first_name']) < 2 or len(info['last_name']) < 2:
            errors.append('Your first and last name must be at least 2 characters long')
        elif not info['first_name'].isalpha() or not info['last_name'].isalpha():
            errors.append('Every character in your first and last name need to be letters')
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')

        query= "SELECT user_level FROM users where id = :id"
        data = {'id': info['queryuser']}
        user = self.db.query_db(query,data)

        if errors:
            return {"status" :False, "errors" :errors}
        elif user[0]['user_level'] == 'admin':
            query = "UPDATE users SET first_name =:first_name, last_name=:last_name, email =:email, updated_at = NOW(), user_level = :user_level WHERE id = :id"
            data ={'id' : info['id'], 'email' : info['email'], 'first_name' : info['first_name'], 'last_name' : info['last_name'], 'user_level': info['user_level']}
        else:
            query = "UPDATE users SET first_name =:first_name, last_name=:last_name, email =:email, updated_at =NOW() WHERE id =:id"
            data ={'id' : info['id'], 'email' : info['email'], 'first_name' : info['first_name'], 'last_name' : info['last_name']}

        self.db.query_db(query,data)
        return {"status" : True}
    def changedesc(self,info):
        data = {'id' : info['id'], 'description' : info['description']}
        query= "UPDATE users SET description=:description, updated_at =NOW() WHERE id=:id"
        self.db.query_db(query,data)
        return {"status" : True}

    def select_messages(self, id):
        query = "SELECT users.active, messages.posted_at, messages.user_id, users.first_name, users.last_name, messages.id, messages.message, messages.created_at FROM users JOIN messages ON user_id = users.id where messages.posted_at =:id ORDER BY messages.created_at DESC "
        data ={
            'id' : id
        }
        return self.db.query_db(query,data)


    def post_message(self, info):
        query = "INSERT INTO messages ( user_id, message, posted_at, created_at, updated_at) VALUES(:user_id, :message, :posted_at, NOW(), NOW())"
        data= {
            'user_id': info['user_id'],
            'message': info['message'],
            'posted_at': info['posted_at']
        }
        self.db.query_db(query,data)

    def select_comments(self):
        query="SELECT users.active, users.first_name, users.last_name,comments.message_id, comments.comment, comments.created_at FROM users JOIN comments ON user_id = users.id ORDER BY comments.created_at ASC"
        return self.db.query_db(query)

    def post_comment(self,info):
        query= "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES(:message_id, :user_id, :comment, NOW(), NOW())"
        data={
            'message_id' :info['message_id'],
            'user_id': info['user_id'],
            'comment': info['comment']
        }
        self.db.query_db(query,data)
    def delete_user(self,id):
        query= "UPDATE users SET active =:active where id =:id" 
        data={
            'id' : id,
            'active' : False
        }
        self.db.query_db(query,data)          
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
