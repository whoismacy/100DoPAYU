from number_guessing_game_art import logo

import random

hard_level_lives = 5
easy_life_lives = 10

def guessing_game(no_of_trials, random_value):
    attempts_taken = 0

    while True:
        guess = int(input("Make a Guess: "))

        if guess < 1 or guess > 100:
            guess = int(input("Kindly enter a value between 1 and 100: "))

        attempts_taken += 1
        
        if no_of_trials < 1:
            print(f"You are out of no_of_lives. [LOSS] !! The number was {random_value}")
            break
        else:
            if guess < random_value:
                print("Your guess is too low.")
                no_of_trials -= 1
            elif guess > random_value:
                print("You guess is too high.")
                no_of_trials -= 1
            elif guess == random_value:
                print(f"Congratulations you did it in {attempts_taken} trial(s) !! The random_value was {random_value}")
                break
        print(f"You have {no_of_trials} attempts remaining.")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
difficulty_level = input("Choose your difficulty: 'hard' or 'easy': ").lower()

if difficulty_level[0] == "h":
    guessing_game(hard_level_lives, random.randint(1, 100))
elif difficulty_level[0] == "e":
    guessing_game(easy_life_lives, random.randint(1, 100))

