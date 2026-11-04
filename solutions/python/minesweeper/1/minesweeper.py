def list_generator(list_of_strings: list[str]):
    list_field: list = [[x for x in y] for y in list_of_strings]
    return list_field


def checker(list_field: list[list[str]]):
    for row_index, row in enumerate(list_field):
        for square_index, square in enumerate(row):
            if square == ' ':
                count = 0
                if row_index != 0:
                    try:
                        if list_field[row_index - 1][square_index - 1] == '*' and square_index != 0:
                            count += 1
                    except:
                        pass
                if row_index != 0:
                    try:
                        if list_field[row_index - 1][square_index] == '*':
                            count += 1
                    except:
                        pass
                if row_index != 0:
                    try:
                        if list_field[row_index - 1][square_index + 1] == '*':
                            count += 1
                    except:
                        pass
                if square_index != 0:
                    try:
                        if list_field[row_index][square_index - 1] == '*':
                            count += 1
                    except:
                        pass
                if square_index != 0:
                    try:
                        if list_field[row_index + 1][square_index - 1] == '*':
                            count += 1
                    except:
                        pass
                try:
                    if list_field[row_index][square_index + 1] == '*':
                        count += 1
                except:
                    pass
                try:
                    if list_field[row_index + 1][square_index] == '*':
                        count += 1
                except:
                    pass
                try:
                    if list_field[row_index + 1][square_index + 1] == '*':
                        count += 1
                except:
                    pass
                if count != 0:
                    list_field[row_index][square_index] = str(count)
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

