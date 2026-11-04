def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    sum = 0
    for number in range(limit):
        for multiple in multiples:
            if multiple != 0 and number % multiple == 0:
                sum += number
                break
    return sum
