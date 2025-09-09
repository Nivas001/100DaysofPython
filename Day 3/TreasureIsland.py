from colorama import Fore, Style

ascii_art = r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     "`=.|                  |
|___________________|__"=._o`"-._        "`=.______________|___________________
          |                "`=._o`"=._      _"`=._                     |
 _________|_____________________:=._o "`=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; "`=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    "`-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o "`=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"`=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"`=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/_____/_____/_____/_____/_____/_____/_____/[Find Treasure]
*******************************************************************************
'''

print(Fore.YELLOW + ascii_art + Style.RESET_ALL)

def get_valid_input(prompt, valid_option):
    while True:
        user_input = input(prompt).upper()
        if user_input in valid_option:
            return user_input
        print(f"You have entered incorrect option. Please choose {', '.join(valid_option)}")


print("Welcome to Treasure Island. \n Your mission is to find the treasure.")
direction = get_valid_input("Left or Right? ", ["LEFT", "RIGHT"])

if direction == "LEFT":
    print("You have came to a lake. There is an island in the middle of the lake.")
    choice = get_valid_input("Type 'wait' to wait for a boat. Type 'swim' to swim across. ", ["WAIT", "SWIM"])

    if choice == "WAIT":
        print("You arrived at the island unharmed. There is a house with 3 doors.")
        door = get_valid_input("One red, One yellow and one blue. Which color do you choose? ", ["RED", "YELLOW", "BLUE"])

        if door == "RED":
            print(Fore.RED + "You have been Burned in fire." + Style.RESET_ALL)
            print(Fore.RED + "!!!!! Game over !!!!!" + Style.RESET_ALL)

        elif door == "YELLOW":
            print(Fore.YELLOW + "You found the treasure." + Style.RESET_ALL)
            print(Fore.YELLOW + "!!! YOU WIN !!!" + Style.RESET_ALL)

        elif door == "BLUE":
            print(Fore.RED + "You have been eaten by BEAST" + Style.RESET_ALL)
            print(Fore.RED + "!!!!! Game Over !!!!!" + Style.RESET_ALL)

        else:
            print(Fore.RED + "GAME OVER"+ Style.RESET_ALL)

    else:
        print(Fore.RED + "Attacked by Trout." + Style.RESET_ALL)
        print(Fore.RED + "!!!! Game over !!!!" + Style.RESET_ALL)

else:
    print(Fore.RED + "Fall into a hole." + Style.RESET_ALL)
    print(Fore.RED + "!!! Game Over !!!" + Style.RESET_ALL)