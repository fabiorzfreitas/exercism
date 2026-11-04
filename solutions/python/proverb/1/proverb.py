from typing import Optional


def middle_sentences(*input_data: list[str]):
    sentence_list: list = []
    for index, word in enumerate(input_data):
        if index < len(input_data) - 1:
            sentence_list.append(f'For want of a {word} the {input_data[index + 1]} was lost.')
    return sentence_list


def last_sentence(word: str, qualifier: Optional[str]=None):
    if qualifier:
        qualifier = f'{qualifier} '
    else:
        qualifier = ''
    return f'And all for the want of a {qualifier}{word}.'


def proverb(*input_data: list[str], qualifier: Optional[str]=None):
    final_list: list = []
    if not input_data:
        return final_list
    if len([*input_data]) > 1:
        final_list: list = middle_sentences(*input_data)
    final_list.append(last_sentence(input_data[0], qualifier))
    return final_list
     
