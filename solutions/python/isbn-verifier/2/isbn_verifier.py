def is_valid(isbn):
    check = []
    for index, digit in enumerate(isbn):
        if digit.isnumeric():
            check.append(digit)
        elif len(check) == 9 and digit.lower() == 'x':
            check.append('10')
        elif digit.isalpha():
            return False
    if len(check) != 10:
        return False
    return (sum((10-i)*int(digit) for i, digit in enumerate(check)) % 11 == 0)
