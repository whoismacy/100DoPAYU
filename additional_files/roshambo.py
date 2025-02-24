import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

roshambo = [rock, paper, scissors]

users_choice = int(input("What do you choose ? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))

print(roshambo[users_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:\n" + roshambo[computer_choice])

if computer_choice == 0:
    if users_choice == 0:
        print("You draw!")
    elif users_choice == 1:
        print("You win!")
    elif users_choice == 2:
        print("You lose!")

elif computer_choice == 1:
    if users_choice == 0:
        print("You lose!")
    elif users_choice == 1:
        print("You draw!")
    elif users_choice == 2:
        print("You win!")

elif computer_choice == 2:
    if users_choice == 0:
        print("You win!")
    elif users_choice == 1:
        print("You lose!")
    elif users_choice == 2:
        print("You draw!")
