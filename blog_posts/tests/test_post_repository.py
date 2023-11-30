from lib.post_repository import *
from lib.posts import *


def test_get_all_posts(db_connection):
    db_connection.seed('seeds/blog_posts_tags.sql')
    repository = PostRepository(db_connection)
    posts = repository.all()

    assert posts == [
        Post(1,'How to use Git'),
        Post(2,'Fun classes'),
        Post(3,'Using a REPL'),
        Post(4,'My weekend in Edinburgh'),
        Post(5,'The best chocolate cake EVER'),
        Post(6,'A foodie week in Spain'),
        Post(7,'SQL basics'),
    ]

def test_find_by_tag(db_connection):
    db_connection.seed('seeds/blog_posts_tags.sql')
    repository = PostRepository(db_connection)
    posts = repository.find_by_tag('coding')

    assert posts == [
        Post(1,'How to use Git'),
        Post(2,'Fun classes'),
        Post(3,'Using a REPL'),
        Post(7,'SQL basics'),
    ]