from lib.database_connection import *
from lib.order_repository import *
from lib.product_repository import *
from datetime import date


class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed('seeds/shop_manager.sql')

    def run(self):
        product_repository = ProductRepository(self._connection)
        order_repository = OrderRepository(self._connection)
        print('Welcome to the shop management program!')
        while True:
            print('\nWhat do you want to do?')
            print(' 1 = list all shop items')
            print(' 2 = create a new item')
            print(' 3 = list all orders')
            print(' 4 = create a new order')
            print(' 5 = see all items in specific order')
            response = input('\nSelect your choice: ')
            if response == '1':
                products = product_repository.all()
                print('\nHere is the list of all shop items:\n')
                for product in products:
                    print(f'#{product.id} {product.name} - Unit Price: £{product.unit_price} - Quantity: {product.quantity}')
            elif response == '2':
                name = input('\nPlease enter the name of the product: ')
                unit_price = input('\nPlease enter the unit price: ')
                quantity = input('\nPlease enter the quantity currently in stock: ')
                product_repository.create(Product(None, name, float(unit_price), int(quantity)))
                print('\nThank you. Product added to shop items.')
            elif response == '3':
                orders = order_repository.all()
                print('\nHere is a list of all current orders:')
                for order in orders:
                    print(f'#{order.id} - customer name: {order.customer_name} - date order placed: {order.order_date}')
            elif response == '4':
                name = input('\nPlease enter the customer\'s name: ')
                order_date = input('\nPlease input the date of the order in the format YYYYMMDD: ')
                order_repository.create(Order(None, name, date(int(order_date[0:4]), int(order_date[4:6]), int(order_date[6:]))))
                print('\nThank you, order created.')
            elif response == '5':
                order_number = input('\nPlease enter the order number for the order you wish to view: ')
                result = order_repository.find_order_with_products(int(order_number))
                customer = order_repository.find_one_order(order_number)
                print('\nOrder for:')
                print(f'Customer ID: {customer.id}, Customer Name: {customer.customer_name}, Order_Date: {customer.order_date}\n')
                for product in result:
                    print(f'Product id: {product.id}, Product name: {product.name}, Quantity ordered: {product.quantity}')
            else:
                print('Please select a valid option')
            done = input('\nWould you like to close the program? Y/N: ')
            if done.upper() == 'Y':
                break
            else:
                continue
        

if __name__ == '__main__':
    app = Application()
    app.run()