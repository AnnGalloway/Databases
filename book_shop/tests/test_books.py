from lib.books import *
"""
Book constructs with an id, title and author name
"""

test_book = Books(1, "book title", "book author")

def test_book_init():
    assert test_book.id == 1
    assert test_book.title == "book title"
    assert test_book.author_name == "book author"

"""
We can format books to strings nicely
"""
def test_book_formats_nicely():
    assert str(test_book) == "Book(1, book title, book author)"

"""
We can compare two identical book and have them be equal
"""
def test_books_are_equal():
    test_book2 = Books(1, "book title", "book author")
    assert test_book == test_book2