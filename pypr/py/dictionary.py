numbers = {} # Creating an empty dictionary

numbers['zero'] = 0 # Creating a dictionary, adding an item at a time
numbers['one'] = 1
numbers['two'] = 2

numbers = {'zero': 0, 'one': 1, 'two': 2} # Can also add all the items at the same time

empty = dict() # We can also create an empty dictionary using the dict() keyword.
numbers_copy = dict(numbers) # Making a copy of an already existent dict, great if you would like modifying the original dict.
print(numbers_copy)


# The 'in' operator works on dictionaries, returns a bool to tell us if sth
# is a key in a dictionary or not, DOES NOT CHECK WHETHER STH IS A VALUE
print('one' in numbers)


# The time it takes to find an element in a list is proportional to the
# length of the list. The time it takes to find an element in a list is
# proportional to the length of the list.

def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

# counter = value_counts("Shem Murimi")
#
# for key in counter:
#     print(key, end='')
#
# print(" ", end='')
#
# for value in counter.values():
#     print(value, end='')

# You can put a list in a dictionary as a value, BUT
d = {4:['r', 'o', 'u', 's']}
print(d)
# You can't put a list in a dictionary as a key.
# unhashable type 'list'
letters = list('abcd')
# d[letters] = 4

# the get() method, takes a key and a default value,  if the key
# appears in the dictionary, get returns the corresponding value;
# otherwise it returns the default value.
