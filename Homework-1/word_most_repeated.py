import re


def count_words(file):
    """Read a file and count the words, Return a dict"""
    file = open(file, "r")
    data = file.read()
    words = re.split(r'[\n ]', data)
    count = {}
    for word in words:
        word_in_lowercase = word.lower()
        if word in count:
            count[word_in_lowercase] += 1
        elif word != '':
            count[word_in_lowercase] = 1
    return count


words_dict = count_words("words.txt")

most_repeated_word = max(words_dict, key=words_dict.get)

print(f"The most repeated word is '{most_repeated_word}' with {words_dict[most_repeated_word]} times")
