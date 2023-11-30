from lib.orders import *
from lib.ordered_product import *

class OrderRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM orders')
        orders = []
        for row in rows:
            item = Order(row['id'], row['customer_name'], row['order_date'])
            orders.append(item)
        return orders
    
    def create(self, order):
        self._connection.execute(
            'INSERT INTO orders (customer_name, order_date) VALUES (%s, %s)',[
                order.customer_name, order.order_date
            ]
        )
    
    def find_one_order(self, order_id):
        rows = self._connection.execute(
            'SELECT * FROM orders WHERE id = %s', [order_id])
        row = rows[0]
        return Order(row['id'], row['customer_name'], row['order_date'])
    
    def find_order_with_products(self, order_id):
        rows = self._connection.execute(
            'SELECT orders.order_date, products.id AS product_id, orders.id AS order_id, orders.customer_name, products.name, products_orders.order_quantity '\
            'FROM products '\
            'JOIN products_orders ON products_orders.product_id = products.id '\
            'JOIN orders ON orders.id = products_orders.order_id '\
            'WHERE orders.id = %s',[order_id])
        products = []
        for row in rows:
            product = OrderedProduct(row['product_id'], row['name'], row['order_quantity'])
            products.append(product)
        return products