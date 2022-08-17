from count_words import count_words

words_dict = count_words("words.txt")

most_repeated_word = max(words_dict, key=words_dict.get)

print(f"The most repeated word is '{most_repeated_word}' with {words_dict[most_repeated_word]} times")