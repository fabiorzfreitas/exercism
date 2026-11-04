def is_paired(input_string):
    brackets = ['[', ']', '(', ')', '{', '}']
    bracket_pairs = ['[]', '()', '{}']
    evaluate = []
    for character in input_string:
        if character in brackets:
            evaluate.append(character)
    evaluate_string = ''.join(evaluate)
    while any(x in evaluate_string for x in bracket_pairs):
        for pair in bracket_pairs:
            evaluate_string = evaluate_string.replace(pair, '')
    return not evaluate_string
