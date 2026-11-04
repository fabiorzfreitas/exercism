letter_values: dict = {
    k:v
    for keys, v in [
    (['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't' ], 1),
    (['d', 'g'], 2),
    (['b', 'c', 'm', 'p'], 3),
    (['f', 'h', 'v', 'w', 'y'], 4),
    (['k'], 5),
    (['j', 'x'], 8),
    (['q', 'z'], 10)
    ]
    for k in keys
}


def score(word):
    return sum([letter_values.get(letter.lower()) for letter in word])

