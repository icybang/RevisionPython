import random

# ASCII art for rock, paper, and scissors
art = {
    0: """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    1: """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    2: """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

# Determine the winner
rules = {
    0: {0: "Draw!", 1: "Lose!", 2: "Win!"},  # Rock
    1: {0: "Win!", 1: "Draw!", 2: "Lose!"},  # Paper
    2: {0: "Lose!", 1: "Win!", 2: "Draw!"}   # Scissors
}

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if user_input >= 0 and user_input <= 2:
    computer_input = random.randint(0, 2)

    print("You chose:")
    print(art[user_input])

    print("Computer chose:")
    print(art[computer_input])

    print(rules[user_input][computer_input])
else:
    print("Invalid input. Please type 0, 1, or 2.")
