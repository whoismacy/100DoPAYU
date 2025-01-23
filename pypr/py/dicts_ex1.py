"""Goal re-write value_counts such
that we eliminate the use of the if-else statement and use get()"""
# get - takes a key and a default value, if the key
# appears in the dictionary, get returns the corresponding value
# otherwise it returns the default value.

def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

def value_counts_exc(string):
    counter = {}
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    return counter

