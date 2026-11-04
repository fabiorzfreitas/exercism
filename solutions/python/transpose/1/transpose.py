def transpose(lines):
    output = []
    output_line = []
    biggest_line_size = max(len(line) for line in lines.split('\n'))
    for index in range(biggest_line_size):
        for line in lines.split('\n'):
            try:
                output_line.append(line[index])
            except:
                output_line.append(' ')
        output.append(''.join(output_line))
        output_line = []
    new_output = []
    for line_index, line in enumerate(output[::-1]):
        new_str = output[- line_index - 1][::-1]
        print(f'outer {line_index}-{new_str}-')
        for char_index, char in enumerate(line[::-1]):
            if char == ' ' and line_index == 0:
                new_str = new_str[:char_index] + new_str[char_index + 1:]
                print(f'line 0 {char_index}-{new_str}-')
            elif char == ' ' and line_index != 0 and output[- line_index][- char_index - 1] == ' ':
                new_str = new_str[:char_index] + new_str[char_index + 1:]
                print(f'line 0+ {char_index}-{new_str}-')                
            else:
                break
        new_output.append(new_str[::-1])

    return '\n'.join(new_output[::-1])
        
print(transpose("\n".join(["The longest line.", "A long line.", "A longer line.", "A line."])))