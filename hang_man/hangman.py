"""This module is a simple hangman game"""
import random

from art_hang_man import stages, logo
from word_dict import word_list

print(logo)

chosen_word = random.choice(word_list)

PLACEHOLDER = ""

game_over = False

correct_letters = []

LIVES = 6

for letter in chosen_word:
    PLACEHOLDER += "_"
print("Word to guess: " + PLACEHOLDER)

while not game_over:

    print("****************************<???>/" + str(LIVES) + " LIVES \
LEFT****************************")

    guess = input("Guess a letter: ").lower()
    DISPLAY = ""

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    for letter in chosen_word:
        if letter == guess:
            DISPLAY += letter
            correct_letters.append(letter)

        elif letter in correct_letters:
            DISPLAY += letter
        else:
            DISPLAY += "_"

    print("Word to guess: " + DISPLAY)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not \
in the word, you lose a life.")

        LIVES -= 1

        if LIVES == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE\
***********************")

    if "_" not in DISPLAY:
        game_over = True
        print("****************************YOU WIN****\
***********************")

    print(stages[LIVES])
