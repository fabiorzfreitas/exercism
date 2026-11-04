from typing import Union
from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name: str, dish_ingredients: list[str]) -> tuple[str, set]:
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name: str, drink_ingredients: list[str]) -> str:
    if set(drink_ingredients).isdisjoint(ALCOHOLS):
        return drink_name + ' Mocktail'
    return drink_name + ' Cocktail'


def categorize_dish(dish_name: str, dish_ingredients: set[str]) -> str:
    dish_types = [(VEGAN, 'VEGAN'), (VEGETARIAN, 'VEGETARIAN'), (PALEO, 'PALEO'), (KETO, 'KETO'), (OMNIVORE, 'OMNIVORE')]
    for variable, name in dish_types:
        if dish_ingredients.issubset(variable):
            return f'{dish_name}: {name}'
    raise ValueError('Unable to categorize dish.')


def tag_special_ingredients(dish: tuple[str, Union[list, set]]) -> tuple[str, set]:
    return (dish[0], set(dish[1]) & SPECIAL_INGREDIENTS)


def compile_ingredients(dishes: list[set]) -> set[str]:
    ingredients: set[str] = set()
    for dish_ingredients in dishes:
        ingredients = ingredients.union(dish_ingredients)
    return ingredients


def separate_appetizers(dishes: list[str], appetizers: list[str]) -> list[str]:
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes: list[set], intersection: set[str]) -> set:
    ingredients: set[str] = set()
    for dish_ingredients in dishes:
        ingredients = ingredients.union(dish_ingredients)
    return ingredients - intersection
