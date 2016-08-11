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
        if not info['name'] or not info['alias']:
            errors.append('Your name and alias cannot be blank')
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

                'name' : info['name'],
                'alias' : info['alias'],
                'email' : info['email'],
                'password' : hashed_pw

            }
            query = "INSERT INTO users (name, alias, email, password, created_at) VALUES(:name, :alias, :email, :password, NOW())"
            self.db.query_db(query,data)
            query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            data = { 'email': info['email'] }
            user = self.db.query_db(query, data)
            return { "status": True, 'id' : user[0]['id'], 'alias': user[0]['alias']}

    def login_user(self,info):
        errors=[]
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = { 'email': info['email'] }
        user = self.db.query_db(query, data) 

        if len(user) < 1:
            errors.append("We do not have your email on file please register")
            return  {'status': False, "errors" : errors}
        elif self.bcrypt.check_password_hash(user[0]['password'], info['password']):
            return { "status": True, 'id' :user[0]['id'], 'alias' : user[0]['alias']}

        else:
            errors.append("We're are sorry but your password did not match our records please try again.")
            return {'status' : False , "errors" : errors }

    def select_recent_reviews(self):
        query="SELECT books.title, reviews.active, reviews.review, reviews.book_id,reviews.rating, reviews.user_id, reviews.created_at, users.name from users join reviews on reviews.user_id = users.id join books on books.id = reviews.book_id order by reviews.created_at DESC LIMIT 3"
        bookreviews = self.db.query_db(query)
        return bookreviews

    def select_books(self):
        query="SELECT title, id from books"
        books= self.db.query_db(query)
        return books

    def select_book(self,id):
        query="SELECT title, author, id from books where id =:id "
        data={'id' : id}
        book=self.db.query_db(query,data)
        return book[0]

    def select_book_reviews(self,id):
        query="SELECT books.title, reviews.id as review_id, reviews.active, reviews.review,reviews.book_id,reviews.rating, reviews.user_id, reviews.created_at, users.name from users join reviews on reviews.user_id = users.id join books on books.id = reviews.book_id where books.id = :id order by reviews.created_at ASC LIMIT 3"
        data={'id': id }
        bookreviews=self.db.query_db(query,data)
        print bookreviews
        return bookreviews

    def delete_review(self,id):
        query= "UPDATE reviews SET active =:active where id =:id" 
        data={
            'id' : id,
            'active' : False
        }
        self.db.query_db(query,data)

    def add_review(self,info):
        query="INSERT INTO reviews(book_id, user_id, rating, review, active, created_at) VALUES(:book_id, :user_id, :rating, :review, :active, NOW())"
        data= {
            'book_id': info['book_id'],
            'user_id' : info['user_id'],
            'rating' : info['rating'],
            'review' : info['review'],
            'active' : True
        } 
        self.db.query_db(query,data)

    def select_user(self, id):
        query ="SELECT * FROM users WHERE id = :id"
        data = {'id': id }
        user = self.db.query_db(query, data)
        if len(user) < 1:
            return False
        else:
            return user[0]

    def user_review(self,id):
        query="SELECT books.title, reviews.active, reviews.book_id, books.id as book_id from users join reviews on reviews.user_id = users.id join books on books.id = reviews.book_id where users.id = :id"
        data= {'id' : id}
        booklist=self.db.query_db(query,data)
        return booklist

    def total_reviews(self,id):
        query="SELECT user_id, count(id) as count from reviews where user_id =:id and active = TRUE group by user_id"
        data = {'id': id}
        total= self.db.query_db(query,data)
        return total[0]

    def author_list(self):
        query="SELECT author from books"
        authors= self.db.query_db(query)
        return authors
    def add_book_and_review(self,info):
        query="INSERT INTO books(title, author, created_at) VALUES(:title, :author, NOW())"
        data= {
            'title' : info['title'],
            'author' : info['author']
        }
        self.db.query_db(query,data)

        query="SELECT id from books order by created_at DESC LIMIT 1"
        bookid=self.db.query_db(query) #print bookid

        query="INSERT INTO reviews(book_id, user_id, rating, review, active, created_at) VALUES(:book_id, :user_id, :rating, :review, :active, NOW())"
        data = {
         'book_id': bookid[0]['id'],
         'user_id': info['user_id'],
         'rating': info['rating'],
         'review': info['review'],
         'active': True

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
