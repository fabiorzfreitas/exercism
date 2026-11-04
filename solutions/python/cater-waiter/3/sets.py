from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name: str, dish_ingredients: list) -> tuple:
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name: str, drink_ingredients: list) -> str:
    if set(drink_ingredients).isdisjoint(ALCOHOLS):
        return drink_name + ' Mocktail'
    return drink_name + ' Cocktail'


def categorize_dish(dish_name: str, dish_ingredients: set) -> str:
    if dish_ingredients.issubset(VEGAN) == True:
        return dish_name + ': VEGAN'
    if dish_ingredients.issubset(VEGETARIAN) == True:
        return dish_name + ': VEGETARIAN'
    if dish_ingredients.issubset(PALEO) == True:
        return dish_name + ': PALEO'
    if dish_ingredients.issubset(KETO) == True:
        return dish_name + ': KETO'
    if dish_ingredients.issubset(OMNIVORE):
        return dish_name + ': OMNIVORE'
    raise ValueError("Unable to categorize dish.")


def tag_special_ingredients(dish: tuple) -> tuple:
    return (dish[0], set(dish[1]) & SPECIAL_INGREDIENTS)


def compile_ingredients(dishes: list) -> set:
    ingredients: set = set()
    for dish_ingredients in dishes:
        ingredients = ingredients.union(dish_ingredients)
    return ingredients


def separate_appetizers(dishes: list, appetizers: list) -> list:
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes: list, intersection: set) -> set:
    ingredients: set = set()
    for dish_ingredients in dishes:
        ingredients = ingredients.union(dish_ingredients)
    return ingredients - intersection
