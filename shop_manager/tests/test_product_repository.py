from lib.products import *
from lib.product_repository import *

def test_get_all_records(db_connection):
    db_connection.seed('seeds/shop_manager.sql')
    repository = ProductRepository(db_connection)
    products = repository.all()

    assert products == [
        Product(1, 'product1', 1.99, 101),
        Product(2, 'product2', 2.99, 102),
        Product(3, 'product3', 3.99, 103),
        Product(4, 'product4', 4.99, 104),
        Product(5, 'product5', 5.99, 105),
    ]

def test_create(db_connection):
    db_connection.seed('seeds/shop_manager.sql')
    repository = ProductRepository(db_connection)
    repository.create(Product(None,'product6', 6.99, 106))
    result = repository.all()
    assert result == [
        Product(1, 'product1', 1.99, 101),
        Product(2, 'product2', 2.99, 102),
        Product(3, 'product3', 3.99, 103),
        Product(4, 'product4', 4.99, 104),
        Product(5, 'product5', 5.99, 105),
        Product(6, 'product6', 6.99, 106),
    ]
