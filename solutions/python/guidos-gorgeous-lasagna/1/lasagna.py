"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40
"""
Constant for comparing elapsed time.
"""

# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME = 2
"""
Constant for layer preparation time.
"""

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(arg):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - arg


# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(arg):

    """Calculate the preparation time according to the number of layers.
    
    :param arg: int - number of layers
    :return: int - time in minutes for preparation
    """
    
    return arg * PREPARATION_TIME

# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):

    """Calculate total elapsed time in minutes.
    
    :param number_of_layers: int - number of layers to prepare
    :param elapsed_bake_time: int - baking elapsed time in minutes
    :return: int - sum of preparation and baking time
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time