from lib.recipe import *

recipe = Recipe(1,"test recipe", 30, 5)

"""
Recipe constructs with an id, name average_cooking_time and rating
"""
def test_recipe_constructs():
    assert recipe.id == 1
    assert recipe.name == "test recipe"
    assert recipe.average_cooking_time == 30
    assert recipe.rating == 5

"""
We can format recipes to strings nicely
"""
def test_recipe_format_nicely():
    assert str(recipe) == "Recipe(1, test recipe, 30, 5)"

"""
We can compare two identical recipes
And have them be equal
"""
def test_recipes_are_equal():
    recipe2 = Recipe(1,"test recipe", 30, 5)
    assert recipe == recipe2
