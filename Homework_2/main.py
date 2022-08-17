# The line below does not work running the app from the terminal
# from Homework_1.count_words import count_words
# The line below does not work running the app from play button on pyCharm, I had to use export PYTHONPATH=’path/to/directory’
from count_words import count_words
import sys

words_dict = count_words("romeo.txt")
is_the_app_running = True


def find_word_count(dictionary, word):
    count = dictionary.get(word.lower(), False)
    if count:
        print(f"The word '{word}' is repeated {count} times")
    else:
        print(f"The word '{word}' was not found")
    print("--------------------------------------------\n")


if len(sys.argv) > 1:
    find_word_count(words_dict, sys.argv[1])

while is_the_app_running:
    print("MENU")
    print("""
    1 - Search the most repeated word in the file
    2 - Search how many times a typed word is repeated
    3 - Exit the program
    """)
    option = input("Choose an option typing the number: ")
    print("")
    if not option.isnumeric():
        print("Choose a valid option!")
        print("--------------------------------------------\n")
    elif int(option) == 1:
        most_repeated_word = max(words_dict, key=words_dict.get)
        print(f"The most repeated word is '{most_repeated_word}' with {words_dict[most_repeated_word]} times")
        print("--------------------------------------------\n")
    elif int(option) == 2:
        word = input("Type a word: ")
        find_word_count(words_dict, word)
    else:
        is_the_app_running = False
        print("Good bye")
        print("--------------------------------------------\n")
