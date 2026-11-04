def list_multiplier(multipliers: list):
    result: int = 1
    for x in multipliers:
        result = result * x
    return result


def square_root(number: int, factors: list[int]=[1], clear=True):
    list_of_factors: list = factors
    if clear:
        list_of_factors: list = []
    while number != 1:
        for i in range(2, number + 1):
            if number % i == 0:
                list_of_factors.append(i)
                return square_root(int(number / i), list_of_factors, False)
    return list_multiplier(list_of_factors[::2])

