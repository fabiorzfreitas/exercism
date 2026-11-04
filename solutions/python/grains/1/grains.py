def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number -1)


def total():
    grains = []
    for i in range(64):
        grains.append(2 ** i)
    return sum(grains)