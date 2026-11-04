def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for d in digits:
        if not 0 <= d < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    number = []
    for i in range(len(digits)):
        number.append(digits[i] * (input_base ** (len(digits) - (i + 1))))
    output = []
    max_position = 0
    for position in range(sum(number)):
        if output_base ** position > sum(number):
            max_position = position - 1
            break
    base_10 = sum(number)
    for n in range(max_position, -1, -1):
        output.append(base_10 // (output_base ** n))
        base_10 = base_10 % (output_base ** n)
    return output