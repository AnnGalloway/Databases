from lib.database_connection import *

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed('seeds/blog_posts_tags.sql')

    def run(self):
        print('testing')
    
if __name__ == '__main__':
    app = Application()
    app.run()