import random

def load_words():
    with open('pdictionary.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

#numbers
def generate_numbers():