import re
from collections import defaultdict

def count_words(sentence):
    clean_sentence: str = re.sub(r'([^A-Za-z0-9]\'|\'[^A-Za-z0-9]|^\'|\'$)', ' ',(re.sub(r'[^A-Za-z0-9\']', ' ', sentence)))
    count: dict[str, int] = defaultdict(int)
    for word in clean_sentence.split():
        count[word.lower()] += 1
    return dict(count)

