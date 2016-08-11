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
        return redirect('/signin')

    def signin(self):
        if not session.has_key('admin'):
            pass
        else:
            return redirect('/dashboard')
        return self.load_view('index.html')

    def signincheck(self):
        login= {
            "email" : request.form['email'],
            "password" : request.form['password']
        }
        login_status= self.models['User'].login_user(login)
        if login_status['status'] == True:
            session['user_id'] = login_status['id']
            session['admin'] = login_status['admin']
            if login_status['admin'] == True:
                return redirect('/dashboard/admin')
            else:
                return redirect('/dashboard')
        else:
            for message in login_status['errors']:
                flash(message, 'login_errors')
            return redirect('/signin')

    def register(self):
        if not session.has_key('admin'):
            pass
        else:
            return redirect('/dashboard')
        return self.load_view('register.html')
    def registercheck(self):
        user = {
             "first_name" : request.form['first_name'],
             "last_name" : request.form['last_name'],
             "email" : request.form['email'],
             "password" : request.form['password'],
             "cf_password" : request.form['cf_password']
        }
        create_status = self.models['User'].create_user(user)
        if create_status['status'] == True:
            session['user_id'] = create_status['id']
            session['admin'] = create_status['admin']
            if create_status['admin'] == True:
                return redirect('/dashboard/admin')
            else:
                return redirect('/dashboard')
        else:
            for message in create_status['errors']:
                flash(message, 'register_errors')
            return redirect('/register')

    def dashboardadmin(self):
        users = self.models['User'].select_all_users()
        newusers=[]
        for user in users:
            user['created_at']=user['created_at'].strftime("%b %dth %Y")
            if user['active'] == True:
                newusers.append(user)
            else:
                pass
        if not session.has_key('admin'):
            return redirect('/')
        elif session['admin'] == False:
            return redirect('/dashboard')
        else:
            return self.load_view('dashboard.html', user_id = session['user_id'], users=newusers)

    def dashboarduser(self):
        users = self.models['User'].select_all_users()
        newusers=[]
        for user in users:
            user['created_at']=user['created_at'].strftime("%b %dth %Y")
            if user['active'] == True:
                newusers.append(user)
            else:
                pass
        if not session.has_key('admin'):
            return redirect('/')
        elif session['admin'] == True:
            return redirect('/dashboard/admin')
        else:
            return self.load_view('dashboard.html', user_id = session['user_id'], users=newusers)
    def new(self):
        if not session.has_key('admin'):
            return redirect('/signin')
        elif session['admin'] != True:
            return redirect('/dashboard')
        else:
            return self.load_view('new.html', user_id = session['user_id'])

    def newcheck(self):
        user = {
             "first_name" : request.form['first_name'],
             "last_name" : request.form['last_name'],
             "email" : request.form['email'],
             "password" : request.form['password'],
             "cf_password" : request.form['cf_password']
        }
        create_status = self.models['User'].create_user(user)
        if create_status['status'] == True:
            flash("Successfully added a user",'success')
            return redirect('/users/new')
        else:
            for message in create_status['errors']:
                flash(message, 'register_errors')
            return redirect('/users/new')

    def show(self,id):
        if not session.has_key('admin'):    
            return redirect('/signin')
        user = self.models['User'].select_user(id)

        if user == False:
            return redirect('/dashboard/admin')
        else:

            user['created_at']=user['created_at'].strftime("%B %dth %Y")
            messages=self.models['User'].select_messages(id)
            comments=self.models['User'].select_comments()
            newmess =[]
            newcomm =[]
            for message in messages:
                if message['active'] == True:
                    message['created_at'] = message['created_at'].strftime("%B %dth %Y")
                    newmess.append(message)
                else:
                    pass
            for comment in comments:
                if comment['active'] == True:
                    comment['created_at'] = comment['created_at'].strftime("%B %dth %Y")
                    newcomm.append(comment)
                else:
                    pass
 
            return self.load_view('profile.html', user=user, user_id=session['user_id'], messages=newmess, comments=newcomm)

    def remove(self,id):
        if not session.has_key('admin'):
            return redirect('/signin')
        elif session['admin'] != True:
            return redirect('/dashboard')
        else:
            user = self.models['User'].select_user(id)
            if user ==  False:
                return redirect('/dashboard')
        if session['user_id'] == int(id):
            session.clear()
            self.models['User'].delete_user(id)
            return redirect('/signin')
        else:
            self.models['User'].delete_user(id)        
            return redirect('/dashboard/admin')

    def adminedit(self,id):
        if not session.has_key('admin'):
            return redirect('/signin')
        elif session['admin'] != True:
            return redirect('/users/edit')
        else:
            user = self.models['User'].select_user(id)
            if user ==  False:
                return redirect('/dashboard/admin')
            else:
                return self.load_view('edit.html', user=user, user_id = session['user_id'])

    def edit(self):
        if not session.has_key('admin'):
            return redirect('/signin')
        else:
            user = self.models['User'].select_user(session['user_id'])

        return self.load_view('edit.html', user = user, user_id = session['user_id'])

    def editpassword(self,id):
        data={
            'id' : id,
            'password' : request.form['password'],
            'cf_password' : request.form['cf_password']
        }
        change_status = self.models['User'].changepass(data)
        if change_status['status'] == True:
            flash("You have successfully updated your password", 'successpass')
        else:
            for message in change_status['errors']:
                flash(message, 'change_errorspass')
        return redirect('users/edit/'+str(id))

    def editname(self,id):
        if session['admin'] == True:
            data={
                'id' : id,
                'email' : request.form['email'],
                'first_name' : request.form['first_name'],
                'last_name' : request.form['last_name'],
                'user_level' : request.form['user_level'],
                'queryuser' : session['user_id']
            }
            change_status=self.models['User'].changename(data)
        else:
            data={
                'id' : id,
                'email' : request.form['email'],
                'first_name' : request.form['first_name'],
                'last_name' : request.form['last_name'],
                'queryuser' : session['user_id']
            }
            change_status=self.models['User'].changename(data)
        if change_status['status'] == True:
            flash("You have successfully updated your information", 'successname')
        else:
            for message in change_status['errors']:
                flash(message, 'change_errorsname')
        return redirect('users/edit/'+str(id))



   
        return redirect('/users/edit'+str(id))
    def editdesc(self,id):
        data = {
            'id' : id,
            'description': request.form['description']
        }
        change_status= self.models['User'].changedesc(data)
        if change_status['status'] == True:
            flash("You have successfully updated your information", 'successdesc')
        return redirect('users/edit/'+str(id))

    def messages(self,posted_at,posted_by):
        data = {
            'user_id': posted_by,
            'posted_at': posted_at,
            'message': request.form['messagecontent']
        }
        print data
        self.models['User'].post_message(data)

        return redirect('users/show/'+str(posted_at))
    def comments(self,message_id,posted_by,posted_at):
        data={
            'user_id': posted_by,
            'comment': request.form['commentcontent'],
            'message_id': message_id
        }
        self.models['User'].post_comment(data)

        return redirect('users/show/'+str(posted_at))

    def logoff(self):
        session.clear()
        return redirect('/')

#seankendrick12@gmail.com
#password123
#caityilek@gmail.com
#nottelling
#patrick@gmail.com
#password123.com







   



