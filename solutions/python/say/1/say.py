def triad_name(triad: str):

    numeral_names: dict = {
        '0': '',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four', 
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    decimal_names: dict = {
        '0': '',
        '2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety'
    }

    special_cases: dict = {
        '0': 'ten',
        '1': 'eleven',
        '2': 'twelve',
        '3': 'thirteen',
        '4': 'fourteen',
        '5': 'fifteen',
        '6': 'sixteen',
        '7': 'seventeen',
        '8': 'eighteen',
        '9': 'nineteen'
    }

    name: str = ''
    for index, char in enumerate(triad.zfill(3)):
        if index == 0 and char != '0':
            name = f'{numeral_names[char]} hundred'
        elif index == 1:
            if char != '1':
                name = f'{name} {decimal_names[char]}'.rstrip()
            elif char == '1':
                name = f'{name} {special_cases[triad.zfill(3)[2]]}'
                return name.lstrip()
        elif index == 2 and triad.zfill(3)[1] != '0' and char != '0':
            name = f'{name}-{numeral_names[char]}'
        elif index == 2 and triad.zfill(3)[1] == '0':
            name = f'{name} {numeral_names[char]}'.rstrip()
    return name.lstrip()
            

def say(number):
    
    if 0 > number or number > 999999999999:
        raise ValueError("input out of range")

    if number == 0:
        return 'zero'

    triads: list = [str(number).zfill(12)[i:i+3] for i in range(0, 11, 3)]
    spelled_number: str = ''

    for index, triad in enumerate(triads):
        if triad != '000':
            if index == 0:
                spelled_number = f'{triad_name(triad)} billion'
            elif index == 1:
                spelled_number = f'{spelled_number} {triad_name(triad)} million'.lstrip()
            elif index == 2:
                spelled_number = f'{spelled_number} {triad_name(triad)} thousand'.lstrip()
            elif index == 3:
                spelled_number = f'{spelled_number} {triad_name(triad)}'.lstrip()
    
    return spelled_number

for i in range(200):
    print(say(i))