"""Goal: A function that takes two dictionaries
{where each maps from a set of letters to number of times they appear.}
and returns a new dictionary that contains all of the letters and total
number of times they appear in either word."""

def value_counts(sequence):
    counter = dict()
    for letter in sequence:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

def total_count(dict1, dict2):
    dictionary = dict()
    for letter in dict1:
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1
    for letter in dict2:
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1
    return dictionary

print(total_count(value_counts("abcd"), value_counts("abcdefgh")))
