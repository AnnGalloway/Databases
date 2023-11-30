from lib.tags import *
from lib.tag_repository import *

def test_find_by_post(db_connection):
    db_connection.seed('seeds/blog_posts_tags.sql')
    repository = TagRepository(db_connection)
    tags = repository.find_by_post(2)

    assert tags == [
        Tag(1, 'coding'),
        Tag(4, 'education')
    ]