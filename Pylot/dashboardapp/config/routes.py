"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes
    
    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter 
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller'] = 'Users' #done
routes['/signin'] = 'Users#signin' #done 
routes['POST']['/signin/check'] = 'Users#signincheck' #done
routes['/register'] = 'Users#register' #done
routes['POST']['/register/check'] ='Users#registercheck' #done
routes['/dashboard/admin'] = 'Users#dashboardadmin' #done
routes['/dashboard'] = 'Users#dashboarduser' #done
routes['/users/new'] = 'Users#new' #done
routes['POST']['/register/admin/check'] = 'Users#newcheck' #done
routes['/users/show/<id>'] = 'Users#show' #done timestamps need work
routes['/users/remove/<id>'] = 'Users#remove' #problem with javascript
routes['/users/edit/<id>'] = 'Users#adminedit'#done
routes['/users/edit'] = 'Users#edit' #done
routes['POST']['/users/editname/<id>'] = 'Users#editname' #done
routes['POST']['/users/editpassword/<id>'] = 'Users#editpassword' #done
routes['POST']['/users/editdesc/<id>'] = 'Users#editdesc' #done
routes['POST']['/messages/post/<posted_at>/<posted_by>'] = 'Users#messages' #done fix timestamp
routes['POST']['/comments/post/<message_id>/<posted_by>/<posted_at>'] = 'Users#comments'#done fix timestamp
routes['/logoff'] = 'Users#logoff' #done





"""
    You can add routes and specify their handlers as follows:

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    Note the '#' symbol to specify the controller method to use.
    Note the preceding slash in the url.
    Note that the http verb must be specified in ALL CAPS.
    
    If the http verb is not provided pylot will assume that you want the 'GET' verb.

    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path). 
    If the type is not specified it will default to string

    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
