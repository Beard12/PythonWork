"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from time import strftime, localtime


class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
    
    def index(self):
        courses = self.models['Course'].get_courses()
        if len(courses) < 1:
            session['check'] == False
        else:
            session['check'] == True
        return self.load_view('index.html', courses=courses)

    def add(self):
        if request.form['coursename'] == "":
            flash("Course name must be completed")
            return redirect('/')
        elif request.form['coursedesc'] == "":
            course_details ={
            'course': request.form['coursename'],
            'description': " "
            }
        else:
            course_details={
            'course': request.form['coursename'],
            'description': request.form['coursedesc']
            }

        self.models['Course'].add_course(course_details)
        return redirect('/')

    def destroy(self,course_id):
        course=self.models['Course'].select_course(course_id)
        return  self.load_view('destroy.html',course=course[0])

    def destroyhtml(self,course_id):
        course_details={
        'id':course_id
        }
        self.models['Course'].delete_course(course_details)
        return redirect('/')




   



