import re

def abbreviate(words: str):
    word_list: list = re.sub(r'-', ' ', (re.sub(r'[^\- A-Za-z]', '', words))).split()
    print(word_list)
    return ''.join([word[0] for word in word_list]).upper()
