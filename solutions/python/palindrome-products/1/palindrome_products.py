def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    palindromes = []
    compare = []
    output = []
    for i in range(min_factor, max_factor + 1):
        for g in range(min_factor, max_factor + 1):
            if g >= i:
                if str(i * g) == str(i * g)[::-1]:
                    palindromes.append([i * g, [i, g]])
                    compare.append(i * g)
    if len(palindromes) == 0:
        return (None, [])
    for entry in palindromes:
        if entry[0] == max(compare):
            output.append(entry[1])
    return (max(compare), output)
    

def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    palindromes = []
    compare = []
    output = []
    for i in range(min_factor, max_factor + 1):
        for g in range(min_factor, max_factor + 1):
            if g >= i:
                if str(i * g) == str(i * g)[::-1]:
                    palindromes.append([i * g, [i, g]])
                    compare.append(i * g)
    if len(palindromes) == 0:
        return (None, [])
    for entry in palindromes:
        if entry[0] == min(compare):
            output.append(entry[1])
    return (min(compare), output)

