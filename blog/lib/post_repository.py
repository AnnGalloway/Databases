from lib.posts import *
from lib.comments import *

class PostRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Post(row['id'], row['title'], row['content'])
            posts.append(item)
        return posts
    
    def find_with_comments(self,post_id):
        rows = self._connection.execute(
            'SELECT posts.id AS post_id, posts.title, posts.content AS post_content, comments.id AS comment_id, comments.content AS comment_content, comments.author '\
            'FROM posts JOIN comments ON posts.id = comments.post_id '\
            'WHERE posts.id = %s', [post_id])
        comments = []
        for row in rows:
            comment = Comment(row['comment_id'], row['comment_content'], row['author'], row['post_id'])
            comments.append(comment)
        return Post(rows[0]['post_id'], rows[0]['title'], rows[0]['post_content'],comments)