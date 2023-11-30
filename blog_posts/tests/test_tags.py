from lib.tags import *

tag = Tag(1,'testing')

"""
Tag contructs with an id and name
"""
def test_tag_construction():
    assert tag.id == 1
    assert tag.name == 'testing'

"""
Tag formats nicely
"""

def test_tag_format_nicely():
    assert str(tag) == 'Tag(1, testing)'

'''
We can compare two identical tags and have them be equal
'''

def test_posts_equal():
    tag2 = Tag(1,'testing')
    assert tag == tag2