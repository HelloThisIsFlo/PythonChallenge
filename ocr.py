from itertools import permutations
import re


def solve():
    find_rare()


def find_rare():
    with open(r'files/ocr') as junk_file:
        # Load text
        junk = junk_file.read()

        # Store the number of occurrence of each character in a dictionary
        occurrence = dict()
        for char in junk:
            n = occurrence.get(char, 0)
            n += 1
            occurrence[char] = n

        # Sort on the number of occurrence,
        occ_list = [(k, v) for k, v in occurrence.items()]

        # Define sort criteria
        def get_second_value(t):
            return t[1]

        occ_sorted = sorted(occ_list, key=get_second_value)

        # After running the program it is clear that the only values rare are the ones with only 1 occurrence
        i = 0
        occ_curated = list()
        while occ_sorted[i][1] == 1:
            occ_curated.append(occ_sorted[i][0])
            i += 1

        # Find if the letters can make an english word
        words = find_permut_english(occ_curated)
        print(occ_curated)
        print("Possible word(s) : ")
        for word in words:
            print(''.join([' - ', word]))


def find_permut_english(word):
    """ Returns a list of words in the english dictionnary based on the possible permutations of a list of characters
    :param word: list of characters
    :return: list of words in the english dictionnary based on the possible permutations
    """
    # Generate the permutations
    permut = [''.join(letter) for letter in permutations(''.join(word))]
    # Check if in Dictionary
    checker = DictChecker()
    result = set()
    for word in permut:
        if checker.is_a_word(word):
            result.add(word)
    return result


class DictChecker:

    def __init__(self):
        with open('dictionary.txt') as dict_file:
            dict_str = dict_file.read()
            self.dict = set(dict_str.split())

    def is_a_word(self, word):
        return word in self.dict


def official_solution():
    with open('ocr') as junk_file:
        junk = junk_file.read()

        # Find all characters that are not "special"
        letters = re.findall("[A-Za-z]", junk)
        print(letters)
