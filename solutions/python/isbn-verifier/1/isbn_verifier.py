def is_valid(isbn):
    check = []
    for digit in isbn:
        if digit.isnumeric() or digit.lower() == 'x':
            check.append(digit)
        elif digit.isalpha():
            return False
    if len(check) != 10:
        return False
    if 'x' in check[0:8] or 'X' in check[0:8]:
        return False
    return ((
            10*int(check[0])
           + 9*int(check[1])
           + 8*int(check[2])
           + 7*int(check[3])
           + 6*int(check[4])
           + 5*int(check[5])
           + 4*int(check[6])
           + 3*int(check[7])
           + 2*int(check[8])
           + 1*int(check[9] if check[9].isnumeric() else 10)
           ) % 11 == 0)
