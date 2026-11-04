def is_pangram(sentence):
    compare = []
    for item in sorted(set(sentence.lower())):
        if item.isalpha():
            compare.append(item)
    return compare == sorted(set('abcdefghijklmnopqrstuvwxyz'))
