from lib.posts import *

post = Post(1,'testing')

"""
Post contructs with an id and title
"""
def test_post_construction():
    assert post.id == 1
    assert post.title == 'testing'

"""
Post formats nicely
"""

def test_post_format_nicely():
    assert str(post) == 'Post(1, testing)'

'''
We can compare two identical posts and have them be equal
'''

def test_posts_equal():
    post2 = Post(1,'testing')
    assert post == post2