"""Module for learning about sets on Exercism."""
from typing import Iterable
from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


DISH_TYPES = [(VEGAN, 'VEGAN'), (VEGETARIAN, 'VEGETARIAN'), (PALEO, 'PALEO'), (KETO, 'KETO'), (OMNIVORE, 'OMNIVORE')]


def clean_ingredients(dish_name: str, dish_ingredients: list[str]) -> tuple[str, set]:
    """Returns dish name and a deduplicated set of ingredients."""
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name: str, drink_ingredients: list[str]) -> str:
    """Categorizes drinks as Cocktail or Mocktail."""
    if set(drink_ingredients).isdisjoint(ALCOHOLS):
        return drink_name + ' Mocktail'
    return drink_name + ' Cocktail'


def categorize_dish(dish_name: str, dish_ingredients: set[str]) -> str:
    """Categorize dishes according to dish types."""
    for variable, name in DISH_TYPES:
        if dish_ingredients.issubset(variable):
            return f'{dish_name}: {name}'
    raise ValueError('Unable to categorize dish.')


def tag_special_ingredients(dish: tuple[str, Iterable]) -> tuple[str, set]:
    """Returns dish name and a set of special ingredients."""
    return (dish[0], set(dish[1]) & SPECIAL_INGREDIENTS)


def compile_ingredients(dishes: list[set]) -> set[str]:
    """Returns a set of all ingredients from all dishes."""
    ingredients: set[str] = set()
    for dish_ingredients in dishes:
        ingredients = ingredients.union(dish_ingredients)
    return ingredients


def separate_appetizers(dishes: list[str], appetizers: list[str]) -> list[str]:
    """Returns a set of dishes without appetizers."""
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes: list[set], intersection: set[str]) -> set:
    """Finds ingredients used in only one dish."""
    ingredients: set[str] = set()
    for dish_ingredients in dishes:
        ingredients = ingredients.union(dish_ingredients)
    return ingredients - intersection
