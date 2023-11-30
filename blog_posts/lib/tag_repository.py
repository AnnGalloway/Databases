from lib.posts import *
from lib.tags import *

class TagRepository:
    def __init__(self,connection):
        self._connection = connection
    
    def find_by_post(self,post_id):
        rows = self._connection.execute(
            'SELECT tags.id, tags.name '\
            'FROM tags '\
            'JOIN posts_tags ON posts_tags.tag_id = tags.id '\
            'JOIN posts ON posts_tags.post_id = posts.id '\
            'WHERE posts.id = %s', [post_id]
        )
        tags = []
        for row in rows:
            tag = Tag(row['id'], row['name'])
            tags.append(tag)
        return tags