from number_guessing_game_art import logo

import random

hard_level_lives = 5
easy_life_lives = 10

def guessing_game(no_of_trials, random_value):
    attempts_taken = 0

    while no_of_trials > 0:
        guess = int(input("Make a guess: "))

        if guess < 1 or guess > 100:
            guess = int(input("Kindly input a value between 1 and 100: "))

        attempts_taken += 1
        
        if guess < random_value:
            no_of_trials -= 1
            print("Your guess is too low.")
            print(f"You have {no_of_trials} attempts remaining.")
        elif guess > random_value:
            no_of_trials -= 1
            print("You guess is too high.")
            print(f"You have {no_of_trials} attempts remaining.")
        elif guess == random_value:
            print(f"Congratulations you did it in {attempts_taken} trial(s) !! The random_value was {random_value}")

    if no_of_trials == 0:
        print(f"You are out of lives. [LOSS] !! The number was {random_value}")

print(logo)
print("Welcome to the Number Guessing Game!")
difficulty_level = input("Choose your difficulty: 'hard' or 'easy': ").lower()
print("I am thinking of a number between 1 and 100")

if difficulty_level[0] == "h":
    guessing_game(hard_level_lives, random.randint(1, 100))
elif difficulty_level[0] == "e":
    guessing_game(easy_life_lives, random.randint(1, 100))

