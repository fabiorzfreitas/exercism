def calculate(answer_eq):
            if answer_eq[1] == 'plus':
                return int(answer_eq[0]) + int(answer_eq[2])
            if answer_eq[1] == 'minus':
                return int(answer_eq[0]) - int(answer_eq[2])
            if answer_eq[1] == 'multiplied':
                return int(answer_eq[0]) * int(answer_eq[2])
            if answer_eq[1] == 'divided':
                return int(answer_eq[0]) / int(answer_eq[2])


def answer(question):
    answer_list = []
    if question.split()[0] == 'Who':
        raise ValueError("unknown operation")
    
    for word in question.rstrip('?').split():
        
        try:
            int(word)
        except:
            pass
        else:
            answer_list.append(word)

        if (
            word == 'plus'
            or word == 'minus'
            or word == 'multiplied'
            or word == 'divided'
            ):
            answer_list.append(word)
        elif word == 'cubed':
            raise ValueError("unknown operation")
    
    print(answer_list)

    if len(answer_list) == 0:
        raise ValueError("syntax error")
    elif len(answer_list) == 1:
        return int(''.join(answer_list))
    
    elif len(answer_list) == 3:
        try:
            int(answer_list[0])
            int(answer_list[2])
        except:
            raise ValueError("syntax error")
        else:
            return calculate(answer_list)

    elif len(answer_list) == 5:
        try:
            int(answer_list[0])
            int(answer_list[2])
            int(answer_list[4])
        except:
            raise ValueError("syntax error")
        else:
            new_list = answer_list[3:]
            first_half = calculate(answer_list[0:3])
            new_list.insert(0, first_half)
            return calculate(new_list)
    else:
        raise ValueError("syntax error")

