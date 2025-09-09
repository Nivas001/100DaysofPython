from colorama import Fore, Style
import random

def get_valid_input(prompt, valid_option):
    while True:
        user_input = input(prompt)
        if user_input in valid_option:
            return int(user_input)
        print(f"Please choose only {' ,'.join(valid_option)}")

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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    ______
---'   ___)_______
          ________)
       ____________)
      (___)
---.__(__)
'''

print("Welcome to ROCK, PAPER and SCISSOR Game !")
user_input = get_valid_input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor: ", ["0", "1", "2"])

options = [rock, paper, scissor]
user_choice = (options[user_input])
print(Fore.BLUE +user_choice +Style.RESET_ALL)

print("\nComputer choose 👇")
random_choice = random.choice(options)
print(Fore.RED + random_choice + Style.RESET_ALL)

comp_index = options.index(random_choice)

#Dictionary Method
results = {
    (0, 0) : "Draw",
    (0, 1) : "You Lose",
    (0, 2) : "You Win",
    (1, 0) : "You Win",
    (1, 1) : "Draw",
    (1, 2) : "You Lose",
    (2, 0) : "You Lose",
    (2, 1) : "You Win",
    (2, 2) : "Draw"
}

print(Fore.YELLOW + results[user_input, comp_index])

#Used for elif for doing this conditions but later found out dictionary method is much better less coding
# if user_choice == random_choice:
#     print("Draw")
# elif user_input == 0 and comp_index == 1:
#     print("You Lose")
# elif user_input == 0 and comp_index == 2:
#     print("You Lose")
# elif user_input == 1 and comp_index == 0:
#     print("You win")
# elif user_input == 1 and comp_index == 2:
#     print("You lose")
# elif user_input == 2 and comp_index == 0:
#     print("You lose")
# elif user_input == 2 and comp_index == 1:
#     print("You win")
