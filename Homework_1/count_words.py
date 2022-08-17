import re
import string


def count_words(file):
    """Read a file and count the words, Return a dict"""
    with open(file, "r") as f:
        data = f.read().translate(str.maketrans('', '', string.punctuation)).lower()
    words = re.split(r'[\n ]', data)
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        elif word != '':
            count[word] = 1
    return count
