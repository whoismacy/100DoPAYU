# TO-DO: We have a list containing a dictionary, so we need a way to fetch the data from the dictionary, and extract the information we require
# TO-DO: How are we going to implement the logic, comparing a player
# if the player loses, we quit the game
# if the player is correct, we take the correct value and compare it to a new one.
# The above is the main question, how am I going to implement it
# A variable that store the user's score, prints it out once the user fails.
# The logo is static and persists throughout the game
# Import the logo and the vs
# Create a global variable, that stores the user's score
# fetch the data
# We need a condition to compare the two pieces of data
# Which one has the largest number of followers.
# Making account at position B become the next account at position A

from higher_lower_art import logo, vs
from higher_lower_data import data

import random

import os

def clear_screen():
    os.system("clear")
    print(logo)

print(logo)
user_score = 0
second_comparison = random.randint(0, len(data) - 1)

while True:
    first_comparison = second_comparison
    second_comparison = random.randint(0, len(data) - 1)

    a_follower_count = data[first_comparison]['follower_count']
    b_follower_count = data[second_comparison]['follower_count']

    print(f"Compare A: {data[first_comparison]['name']}, a {data[first_comparison]['description']}, from {data[first_comparison]['country']}.")
    print(vs)
    print(f"Against B: {data[second_comparison]['name']}, a {data[second_comparison]['description']}, from {data[second_comparison]['country']}.")

    user_input = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_input == "A":
        if a_follower_count > b_follower_count:
            user_score += 1
            clear_screen()
            print(f"You're right! Current score: {user_score}")
        else:
            clear_screen()
            print(f"Sorry, that's wrong. Final score: {user_score}")
            break
    if user_input == "B":
        if b_follower_count > a_follower_count:
            user_score += 1
            clear_screen()
            print(f"You're right! Current score: {user_score}")
        else:
            clear_screen()
            print(f"Sorry, that's wrong. Final score: {user_score}")
            break
