from lib.products import *

class ProductRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM products')
        products = []
        for row in rows:
            item = Product(row['id'], row['name'], row['unit_price'], row['quantity'])
            products.append(item)
        return products
    
    def create(self, product):
        self._connection.execute(
            'INSERT INTO products (name, unit_price, quantity) VALUES (%s, %s, %s)',[
                product.name, product.unit_price, product.quantity
            ]
        )