import copy

def formatter(list_of_lists):
    working_copy = copy.deepcopy(list_of_lists)
    for row_index, row in enumerate(list_of_lists):
        for char_index, char in enumerate(row[::-1]):
            if char_index == 0:
                if char == None:
                    del working_copy[row_index][- 1]
            elif char == None and list_of_lists[row_index][- char_index] == None:
                del working_copy[row_index][- 1]
            else:
                break
    return working_copy


def cleaner(working_copy):
    output = []
    for row in working_copy:
        new_row = []
        for item in row:
            if item != None:
                new_row.append(item)
            else:
                new_row.append(' ')
        output.append(''.join(new_row))
    return '\n'.join(output)
    


def transpose(lines):
    list_of_lines = [line for line in lines.split('\n')]
    list_of_lists = []
    for index in range(len(max(list_of_lines, key=len))):
        list_of_chars = []
        for line in list_of_lines:
            try:
                list_of_chars.append(line[index])
            except:
                list_of_chars.append(None)
        list_of_lists.append(list_of_chars)
    return cleaner(formatter(list_of_lists))

