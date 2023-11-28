from lib.posts import *

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Posts(row['id'], row['title'], row['content'], row['views'], row['user_account_id'])
            posts.append(item)
        return posts

    def create(self,post):
        self._connection.execute(
            'INSERT INTO posts (title, content, views, user_account_id) VALUES (%s, %s, %s, %s)',
                [post.title, post.content, post.views, post.user_account_id]
        )
        return None
    
    def delete(self,id):
        self._connection.execute(
            'DELETE FROM posts WHERE id = %s', [id])
        return None