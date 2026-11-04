def test_against_prime_list(number_to_test: int, prime_list: list[int]) -> bool:
    list_to_test: list[int] = []
    for number in prime_list:
        if number ** 2 <= number_to_test:
            list_to_test.append(number)
        else:
            break
    for prime in list_to_test:
        if number_to_test % prime == 0:
            return False
    return True


def prime(number: int) -> int:
    if number < 1:
        raise ValueError('there is no zeroth prime')
    prime_list: list[int] = []
    count: int = 0
    prime_num: int = 2
    while count < number:
        if test_against_prime_list(prime_num, prime_list):
            prime_list.append(prime_num)
            count += 1
        prime_num += 1
    return prime_list[number - 1]

