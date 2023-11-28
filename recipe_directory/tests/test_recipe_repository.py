from lib.recipe import *
from lib.recipe_repository import *

"""
When we call RecipeRepository#all
We get a list of Recipe objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/recipe_book.sql")
    repository = RecipeRepository(db_connection)

    recipes = repository.all()

    # Assert on the results
    assert recipes == [
        Recipe(1, 'food1', 5, 4),
        Recipe(2, 'food2', 20, 3),
        Recipe(3, 'food3', 30, 5),
        Recipe(4, 'food4', 40, 2),
        Recipe(5, 'food5', 50, 1),
    ]

"""
When we call RecipeRepository#find
We get a single Recipe object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/recipe_book.sql")
    repository = RecipeRepository(db_connection)

    recipe = repository.find('food1')
    assert recipe == Recipe(1, 'food1', 5, 4)
