from lib.posts import *
from lib.post_repository import *

'''
test all
'''
def test_get_all_records(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    posts = repository.all()
    assert posts == [
        Posts(1,'title1', 'content1', 4, 1),
        Posts(2,'title2', 'content2', 100, 1),
        Posts(3,'title3', 'content3', 6, 2),
        Posts(4,'title4', 'content4', 5, 3),
    ]


"""
When we call PostRepository#Create
We get a new record in the database
"""
def test_create_record(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)

    repository.create(Posts(None, 'title5', 'content5', 100, 5))
    result = repository.all()

    assert result == [
        Posts(1,'title1', 'content1', 4, 1),
        Posts(2,'title2', 'content2', 100, 1),
        Posts(3,'title3', 'content3', 6, 2),
        Posts(4,'title4', 'content4', 5, 3),
        Posts(5,'title5', 'content5', 100, 5),
    ]


"""
When we call PostRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        Posts(1,'title1', 'content1', 4, 1),
        Posts(2,'title2', 'content2', 100, 1),
        Posts(4,'title4', 'content4', 5, 3),
    ]