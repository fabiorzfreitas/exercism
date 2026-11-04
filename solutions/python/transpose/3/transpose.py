def formatter(list_of_lists):
    for row_index, row in enumerate(list_of_lists):
        for  char in row[::-1]:
            if char == None:
                list_of_lists[row_index].pop()
            else:
                break
    return list_of_lists


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
    list_of_lines = lines.split('\n')
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


print(transpose("\n".join(["The longest line.", "A long line.", "A longer line.", "A line."])))