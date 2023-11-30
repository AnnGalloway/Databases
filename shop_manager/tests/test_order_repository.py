from datetime import date
from lib.order_repository import *

d1 = date(2023,1,1)


def test_get_all_records(db_connection):
    db_connection.seed('seeds/shop_manager.sql')
    repository = OrderRepository(db_connection)
    orders = repository.all()
    assert orders == [
        Order(1, 'customer1', date(2023,1,1)),
        Order(2, 'customer2', date(2023,1,2)),
        Order(3, 'customer3', date(2023,1,3)),
        Order(4, 'customer4', date(2023,1,4))
    ]

def test_create(db_connection):
    db_connection.seed('seeds/shop_manager.sql')
    repository = OrderRepository(db_connection)
    repository.create(Order(None, 'customer5', date(2023,1,5)))
    orders = repository.all()
    assert orders == [
        Order(1, 'customer1', date(2023,1,1)),
        Order(2, 'customer2', date(2023,1,2)),
        Order(3, 'customer3', date(2023,1,3)),
        Order(4, 'customer4', date(2023,1,4)),
        Order(5, 'customer5', date(2023,1,5)),
    ]

def test_find_order_with_products(db_connection):
    db_connection.seed('seeds/shop_manager.sql')
    repository = OrderRepository(db_connection)
    order = repository.find_order_with_products(1)
    assert order == Order(1, 'customer1', date(2023,1,1), [
        OrderedProduct(1, 'product1', 1),
        OrderedProduct(4, 'product4', 1),
        OrderedProduct(5, 'product5', 1)
    ])