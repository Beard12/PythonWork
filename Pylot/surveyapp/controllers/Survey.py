"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Survey(Controller):
    def __init__(self, action):
        super(Survey, self).__init__(action)
    def index(self):
        
        return self.load_view('index.html')
    def process(self):
        session['name'] = request.form['name']
        session['dojlocation'] = request.form['dojlocation']
        session['favlang']= request.form['favlang']
        session['comment']= request.form['comment']

        if not session.has_key('count'):
            session['count'] =0
        session['count'] +=1 
        return redirect('/survey/result')
    def result(self):

        return self.load_view('result.html')
   



