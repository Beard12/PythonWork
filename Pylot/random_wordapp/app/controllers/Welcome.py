"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
import string
import random
from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
    def index(self):
        string.letters
        if not session.has_key('count'):
            session['count']=1

        newstr=""
        for x in xrange(0,14):
            char = random.choice(string.letters)
            newstr+= char
        
        return self.load_view('index.html', number=session['count'], ranstring=newstr)
    def generate(self):
        session['count']+=1
        return redirect('/')
   



