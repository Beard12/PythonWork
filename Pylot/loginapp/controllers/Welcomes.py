"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *



class Welcomes(Controller):
    def __init__(self, action):
        super(Welcomes, self).__init__(action)
        self.load_model('Welcome')
    
    def index(self):
        if not session.has_key('name'):
            return self.load_view('index.html')
        else:
            return redirect('/success')
            

    def register(self):
        user = {
             "first_name" : request.form['first_name'],
             "last_name" : request.form['last_name'],
             "email" : request.form['email'],
             "password" : request.form['password'],
             "cf_password" : request.form['cf_password']
        }
        create_status = self.models['Welcome'].create_user(user)
        if create_status['status'] == True:
            session['name'] = request.form['first_name'] 
            session['message'] = "registered"
            return redirect('/success')
        else:
            for message in create_status['errors']:
                flash(message, 'register_errors')

            return redirect('/')

    def login(self):
        login= {
            "email" : request.form['email'],
            "password" : request.form['password']
        }
        login_status= self.models['Welcome'].login(login)
        if login_status['status'] == True:
            session['message'] = "logged on"
            session['name'] = login_status['name']
            return redirect('/success')
        else:
            for message in login_status['errors']:
                flash(message, 'login_errors')
            return redirect('/')

    def success(self):

        return self.load_view('success.html', user_name = session['name'], message= session['message'])

    def logout(self):
        session.clear()
        return redirect('/')




   



