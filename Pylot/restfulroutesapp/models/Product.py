""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model


class Product(Model):
    def __init__(self):
        super(Product, self).__init__()

    def get_products(self):
        query = "SELECT * FROM products"
        return self.db.query_db(query)

    def create_product(self, product):
        query = "INSERT into products (name, description, price) VALUES(:name, :description, :price) "
        data={'name': product['name'], 'description': product['description'], 'price' : product['price']}
        self.db.query_db(query,data)
        
    def show_product(self,product):
        query = "SELECT * FROM products WHERE id = :id"
        data = {'id' : product['id']}
        return self.db.query_db(query,data)
    def update_product(self,product):
        query = "UPDATE products SET name = :name, description = :description, price = :price WHERE id = :id"
        data ={'id': product['id'], 'name': product['name'], 'description' : product['description'], 'price' :product['price']}
        self.db.query_db(query,data)

    def delete_product(self,product):
        query = "DELETE FROM products WHERE id = :id"
        data = {'id' : product['id']}
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