def is_armstrong_number(number):
    digits = []
    for i in str(number):
        digits.append(int(i) ** len(str(number)))
    return sum(digits) == number
