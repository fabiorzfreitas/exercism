def factors(number, min_factor, max_factor):
    factor_list = []
    for i in range(min_factor, round(int(number ** (1/2))) + 2):
        for j in range(min_factor, max_factor + 1):
            if i <= j:
                if i * j == number:
                    factor_list.append([i, j])
    return factor_list


def largest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    for number in range((max_factor ** 2), (min_factor ** 2) -1,-1):
        if str(number) == str(number)[::-1]:
            for factor in range(min_factor, max_factor + 1):
                if number % factor == 0 and min_factor <= number / factor <= max_factor:
                    if min_factor <= number <= max_factor:
                        new_factors = factors(number, min_factor, max_factor)
                        new_factors.append([1, number])
                        return (number, new_factors)
                    else:
                        return (number, factors(number, min_factor, max_factor))
    return (None, [])
    

def smallest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    for number in range(min_factor ** 2, (max_factor ** 2) +1):
        if str(number) == str(number)[::-1]:
            for factor in range(min_factor, max_factor + 1):
                if number % factor == 0 and min_factor <= number / factor <= max_factor:
                    if min_factor <= number <= max_factor:
                        new_factors = factors(number, min_factor, max_factor)
                        new_factors.append([1, number])
                        return (number, new_factors)
                    else:
                        return (number, factors(number, min_factor, max_factor))
    return (None, [])

    