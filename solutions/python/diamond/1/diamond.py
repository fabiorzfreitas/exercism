def populate(letter: str):
    list_of_row_lists: list = [[' ' for i in range(((ord(letter) - 64) * 2 ) - 1)] for i in range(ord(letter) - 64)]
    return list_of_row_lists


def upper_half(list_of_lists: list, letter: str):
    for i in range(ord(letter) - 64):
        list_of_lists[i][(ord(letter) - 64) - 1 - i] = chr(ord(letter) - ((ord(letter) - 64 - 1) - i))
        list_of_lists[i][(ord(letter) - 64) - 1 + i] = chr(ord(letter) - ((ord(letter) - 64 - 1) - i))
    return list_of_lists


def mirror(upper_half: list, letter: str):
    mirrored: list = upper_half.copy()
    for i in range(ord(letter) - 64 - 1):
        mirrored.append(upper_half[-2 -i])
    return mirrored


def rows(letter: str):
    diamond = [''.join(row) for row in mirror(upper_half(populate(letter), letter), letter)]
    return diamond

