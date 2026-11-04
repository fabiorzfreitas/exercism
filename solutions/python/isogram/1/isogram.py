def is_isogram(string):
    return sorted(list(i for i in string.lower() if i.isalpha())) == sorted(set(i for i in string.lower() if i.isalpha()))
