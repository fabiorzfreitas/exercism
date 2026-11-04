def is_valid(isbn):
    check = [digit for digit in isbn if digit.isalpha() or digit.isnumeric()]
    if len(check) != 10:
        return False
    if check[-1].lower() == 'x':
        check[-1] = '10'
    if any(i.isalpha() for i in check):
        return False
    return sum((10 - i) * int(digit) for i, digit in enumerate(check)) % 11 == 0