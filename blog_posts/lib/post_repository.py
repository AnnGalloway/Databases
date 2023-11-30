from lib.posts import *
from lib.tags import *


class PostRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Post(row['id'], row['title'])
            posts.append(item)
        return posts
    
    def find_by_tag(self, tag):
        rows = self._connection.execute(
            'SELECT posts.id, posts.title '\
            'FROM posts '\
            'JOIN posts_tags ON posts_tags.post_id = posts.id '\
            'JOIN tags ON posts_tags.tag_id = tags.id '\
            'WHERE tags.name = %s', [tag])
        posts = []
        for row in rows:
            post = Post(row['id'], row['title'])
            posts.append(post)
        return posts
    