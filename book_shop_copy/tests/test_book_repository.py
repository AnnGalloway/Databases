from lib.books import *
from lib.book_repository import *

"""
When we call BookRepository#all
We get a list of Books objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    books = repository.all()

    assert books == [
        Books(1, "Nineteen Eighty-Four", "George Orwell"),
        Books(2, "Mrs Dalloway", "Virginia Woolf"),
        Books(3, "Emma", "Jane Austen"),
        Books(4, "Dracula", "Bram Stoker"),
        Books(5, "The Age of Innocence", "Edith Wharton")
    ]