"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from time import strftime, localtime
import datetime



class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')

    def index(self):
        if not session.has_key('user_id'):
            return self.load_view('index.html')
        else:
            return redirect('/books')

    def signincheck(self):
        login= {
            "email" : request.form['email'],
            "password" : request.form['password']
        }
        login_status= self.models['User'].login_user(login)
        if login_status['status'] == True:
            session['user_id'] = login_status['id']
            session['alias']= login_status['alias']
            return redirect('/books')

        else:
            for message in login_status['errors']:
                flash(message, 'login_errors')
            return redirect('/')

    def registercheck(self):
        user = {
             "name" : request.form['name'],
             "alias" : request.form['alias'],
             "email" : request.form['email'],
             "password" : request.form['password'],
             "cf_password" : request.form['cf_password']
        }
        create_status = self.models['User'].create_user(user)
        if create_status['status'] == True:
            session['user_id'] = create_status['id']
            session['alias']= create_status['alias']
            return redirect('/books')
        else:
            for message in create_status['errors']:
                flash(message, 'register_errors')
            return redirect('/')

    def books(self):
        bookreviews= self.models['User'].select_recent_reviews()
        books= self.models['User'].select_books()
        return self.load_view('books.html', bookreviews= bookreviews ,user=session['alias'],booklist = books)

    def bookhomepage(self,id):
        bookinfo= self.models['User'].select_book(id)
        bookreviews=self.models['User'].select_book_reviews(id)

        return self.load_view('bookpage.html', bookinfo=bookinfo, bookreviews=bookreviews,user=int(session['user_id']))

    def book_review(self,bookid,userid):
        data={
            'user_id': userid,
            'book_id': bookid,
            'rating' : request.form['rating'],
            'review' : request.form['reviewcontent']
        }
        print data
        self.models['User'].add_review(data)
        return redirect('/books/'+str(bookid))

    def delete_review(self,reviewid,bookid):
        self.models['User'].delete_review(reviewid)
        return redirect('/books/'+str(bookid))

    def userhomepage(self,id):
        user= self.models['User'].select_user(id)
        if user == False:
            return redirect('/books')
        count= self.models['User'].total_reviews(id)
        booklist=self.models['User'].user_review(id)
        return self.load_view('userpage.html', user=user, count=count,booklist=booklist)

    def addbook(self):
        authors=self.models['User'].author_list()
        return self.load_view('addbook.html', authors = authors)
    def addbookreview(self):
        if request.form['authornamealt'] == "": #print empty form data cheeck statement
            author = request.form['authorname']
        else:
            author = request.form['authornamealt']
        data = {
            'title' : request.form['title'],
            'author': author,
            'review': request.form['reviewcontent'],
            'rating': request.form['rating'],
            'user_id': session['user_id']
        }
        self.models['User'].add_book_and_review(data)
        return redirect('/books')
    def logoff(self):
        session.clear()
        return redirect('/')




    






   



