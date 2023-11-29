from lib.post_repository import *
from lib.posts import *
from lib.comments import *

def test_get_all_posts(db_connection):
    db_connection.seed('seeds/blog.sql')
    repository = PostRepository(db_connection)
    posts = repository.all()

    assert posts == [
        Post(1,'Post1', 'content1'),
        Post(2,'Post2', 'content2'),
        Post(3,'Post3', 'content3'),
        Post(4,'Post4', 'content4'),
    ]

def test_find_with_comments(db_connection):
    db_connection.seed('seeds/blog.sql')
    repository = PostRepository(db_connection)
    post = repository.find_with_comments(1)
    assert post == Post(1, 'Post1', 'content1', [
        Comment(1, 'content1', 'person1', 1),
        Comment(2, 'content2', 'person2', 1),
    ])