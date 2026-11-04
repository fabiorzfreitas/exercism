def list_generator(list_of_strings: list[str]):
    list_field: list = [[x for x in y] for y in list_of_strings]
    return list_field


def counter(list_field: list[list[str]], row_index: int, square_index: int):
    count: int = 0
    combinations: list = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for row_number, square_number in combinations:
        if row_index + row_number >= 0 and square_index + square_number >= 0:
            try:
                if list_field[row_index + row_number][square_index + square_number] == '*':
                    count += 1
            except:
                pass
    if count != 0:
        list_field[row_index][square_index] = str(count)


def checker(list_field: list[list[str]]):
    for row_index, row in enumerate(list_field):
        for square_index, square in enumerate(row):
            if square == ' ':
                counter(list_field, row_index, square_index)
    return list_field


def annotate(minefield):
    for index, row in enumerate(minefield):
        if len(row) != len(minefield[index - 1]):
            raise ValueError("The board is invalid with current input.")
        for square in row:
            if not square in [' ', '*']:
                raise ValueError("The board is invalid with current input.")
    new_string_list: list[str] = [''.join(x) for x in checker(list_generator(minefield))]
    return new_string_list

