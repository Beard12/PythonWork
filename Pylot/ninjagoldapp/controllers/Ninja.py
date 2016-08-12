"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from time import strftime, localtime
import random

class Ninja(Controller):
    def __init__(self, action):
        super(Ninja, self).__init__(action)
    def index(self):
        if not session.has_key('usergold'):
            session['usergold']=0
        if not session.has_key('activities'):
            session['activities']=[]
            session['classname']=[]
            session['dictionlen']=len(session['activities'])
        
        return self.load_view('index.html', usergold= session['usergold'])
    def process(self, building_id):

        time=strftime("%Y/%m/%d %I:%M %p", localtime())
        session['check'] = True
        if building_id == 'farm':
            money = random.randint(10,20)
            session['usergold'] += money
            session['activities'].append('Earned ' + str(money) + ' golds from the farm!' + '( ' + str(time) + ')')
            session['classname'].append("greentext")
        elif building_id == 'cave':
            money = random.randint(5,10)
            session['usergold'] += money
            session['activities'].append('Earned ' + str(money) + ' golds from the cave!' + '( ' + str(time) + ')')
            session['classname'].append("greentext")
        elif building_id == 'house':
            money = random.randint(2,5)
            session['usergold'] += money
            session['activities'].append('Earned ' + str(money) + ' golds from the house!' + '( ' + str(time) + ')')
            session['classname'].append("greentext")
        elif building_id == 'casino':
            money= random.randint(-50,50)
            if money >= 0: 
                session['usergold'] += money
                session['activities'].append('Earned ' + str(money) + ' golds from the casino!' + '( ' + str(time) + ')')
                session['classname'].append("greentext")
            else:
                session['usergold'] += money
                session['activities'].append('Entered a casino and lost ' + str(money) + ' golds... Ouch.. ' + '( ' + str(time) + ')')
                session['classname'].append("redtext")

        session['dictionlen']+=1


        return redirect('/')

   



