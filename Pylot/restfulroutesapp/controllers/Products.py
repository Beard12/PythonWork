"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *



class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')

    def index(self):
        return redirect('/products')

    def products(self):
        products = self.models['Product'].get_products()
        return self.load_view('index.html', products = products)

    def new(self):
        return self.load_view('create.html')

    def create(self):
        product_data = {
        'name' : request.form['productname'],
        'description' : request.form['productdesc'],
        'price' : request.form['productprice']
        }

        self.models['Product'].create_product(product_data)
        return redirect('/')

    def show(self, product_id):
        product_data = {
        'id' : product_id
        }
        product= self.models['Product'].show_product(product_data)
        return self.load_view('info.html', product= product[0])

    def edit(self, product_id):
        product_data = {
        'id' : product_id
        }
        product= self.models['Product'].show_product(product_data)
        return self.load_view('edit.html', product= product[0])

    def update(self, product_id):
        product_data = {
        'id' : product_id,
        'name' : request.form['productname'],
        'description' : request.form['productdesc'],
        'price' : request.form['productprice']
        }
        self.models['Product'].update_product(product_data)
        
        return redirect('/')

    def destroy(self,product_id):
        product_data = {
        'id' : product_id,
        }
        product=self.models['Product'].delete_product(product_data)
        return redirect('/')





   



