"""Goal: a function that loops a dictionary that maps key->value, loops
through the dictionary and return a list of keys with counts greater than 1"""

def value_counts(sequence):
    counter = dict()
    for letter in sequence:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

def find_repeats(sequence):
    repeats = list()
    dictionary = value_counts(sequence)

    for key in dictionary:
        if dictionary[key] > 1:
            repeats.append(key)
    return repeats


def find_non_repeats(sequence):
    non_repeats = list()
    dictionary = value_counts(sequence)

    for key in dictionary:
        if dictionary[key] <= 1:
            non_repeats.append(key)
    return repeats

print("Repeats: ")
print(find_repeats("the quick brown fox jumped over the lazy dogs"))
print("\nNon-repats: ")
print(find_non_repeats("the quick brown fox jumped over the lazy dogs"))
