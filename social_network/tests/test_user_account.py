from lib.user_account import *
user_account = UserAccount(1,'test e-mail', 'test username')
user_account2 = UserAccount(1,'test e-mail', 'test username')

"""
user_account constructs with an id, email and username
"""
def test_user_account_constructs():
    assert user_account.id == 1
    assert user_account.email == "test e-mail"
    assert user_account.username == "test username"

"""
We can format artists to strings nicely
"""
def test_user_account_format_nicely():
    assert str(user_account) == "UserAccount(1, test e-mail, test username)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_user_accounts_are_equal():
    assert user_account == user_account2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.