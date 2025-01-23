"""Goal: write a function that takes a sequence(list /string)
and returns True if there is any element that appears in the sequence
more than once"""

def value_counts(string):
    counter = dict()

    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

def has_duplicates(sequence):
    counter = value_counts(sequence)
    for key in counter:
        if counter[key] > 1:
            return True
    return False

print(has_duplicates("abcdefghijklmnopqrstuvwxyz"))
