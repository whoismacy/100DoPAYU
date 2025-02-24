import pandas

# Conditional Dictionary Comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test)

# TODO 1: Create a dictionary in the format A="alpha" B="Balls"
# TODO 2: Create a list of the phonetic words that the user inputs
# TODO 0: use iterrows() from pandas

nato = pandas.read_csv("nato_alphabet.csv")
nato_dict = {rows.letter:rows.code for index, rows in nato.iterrows()}

def gen_phonetic():
    user_input = input("Enter the phrase: ").upper()
    try:
        nato_list1 = [nato_dict[letter] for letter in user_input ]
    except KeyError:
        print("Sorry, only letters in the Alphabet please.")
        gen_phonetic()
    else:
        print(nato_list1)


gen_phonetic()
