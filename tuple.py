"""Tuples"""

t = 'l', 'u', 'p', 'i', 'n'
# To create a tuple with a single element, we have to include a final comma:
t1 = 'p',
# The + operator concatenates tuples
# The * operator duplicates tuples a given no. of times
# The sorted function works with tuples but the result is a list
# Same with the reversed function
# Tuples also don't have any of the methods that modify lists (append, remove)

tuple1 = 'a', 'd', 'e', 'b', 'z', 'y', 'o', 'q', 's'
# print(sorted(tuple1))
# print(reversed(tuple1))

email = "johndoe@gmail.com"
email2 = "franksmith123@gmail.com"
email3 = "pythonbarista@gmail.com"

username, domain = email.split('@')
username2, domain2 = email.split('@')
username3, domain3 = email.split('@')

# d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7}
#
# for key,value in d.items():
#     print(key, '->', value)

def min_max(t):
    return min(t), max(t)

list_num = [2, 134, 52, 10, 19, 20, 28, 27, 13, 14, 15, 32, 71, 9, 90]
lowest, highest = min_max(list_num)
# print(lowest, highest)

def mean(*args):
    return sum(args) / len(args)

def trimmed_mean(*args):
    max, min = min_max(args)
    arg_list = list(args)
    arg_list.remove(max)
    arg_list.remove(min)
    return mean(*arg_list)

# print("The trimmed mean is : ", end='')
# print(trimmed_mean(1, 2, 3, 10))

scores1 = [1, 2, 4, 5, 1, 5, 2]
scores2 = [5, 5, 2, 2, 5 ,2 ,3]

# for pair_vals in zip(scores1, scores2):
#     print(pair_vals)

t1_wins = 0

for t1, t2 in zip(scores1, scores2):
    if t1 > t2:
        t1_wins += 1

if t1_wins > len(scores1):
    print("Team 1 wins")
elif t1_wins < len(scores1):
    print("Team 2 wins")
else:
    print("Draw")

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))

# enumerate(sequence), loops through the elements of a sequence and their indices
for index, element in enumerate(letter_map):
    print(index, element)
