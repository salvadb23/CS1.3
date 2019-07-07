
from search import binary_search_iterative
from random import shuffle
from math import factorial
from itertools import permutations 

def get_words(file):
    words = open(file, 'r')
    wordList = words.read().split()
    words.close()
    return wordList

def create_word_array():
    word_arr = []
    for word in get_words('/usr/share/dict/words'):
        word_arr.append(word.lower())
    return word_arr


def get_permutations(string):
    perms = []
    permList = permutations(string)
    for perm in permList:
        string = ''.join(perm)
        perms.append(string)
    return perms
    # word_factorial = factorial(len(string))
    # while len(perm_array) < word_factorial:
    #     word_array = list(string)
    #     shuffle(word_array)
    #     word = ''.join(word_array)
    #     if word not in perm_array:
    #         perm_array.append(word)
    # return perm_array

def unscramble(string):
    word_arr = create_word_array()
    permutations_arr = get_permutations(string.lower())
    unscrambled = []
    for word in permutations_arr:
        if binary_search_iterative(word_arr, word) is not None:
            unscrambled.append(word)
    return unscrambled

print(unscramble('ioskk'))
