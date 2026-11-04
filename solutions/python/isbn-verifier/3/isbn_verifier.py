def is_valid(isbn):
    check = [digit for digit in isbn if digit.isalpha() or digit.isnumeric()]
    print(check[0:9])
    if ( # This if statement should only return False if one of the Fail conditions is met, it curently fails everytime
        (len(check) != 10) # Fail if wrong length
     or (digit.lower() == 'x' for digit in check[0:9]) # Fails if X is found in the first 9 digits
     or (digit.isalpha() and digit.lower() != 'x' for digit in check) # Fail if non-x letter is found
       ):
        return False
    if check[9].lower() == 'x':
        check[9] = '10'
    return sum((10 - i)*int(digit) for i, digit in enumerate(check)) % 11 == 0