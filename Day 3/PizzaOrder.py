print("Welcome to Pizza kadai")

def get_proper_input(prompt, valid_options):
    while True:
        user_input = input(prompt).upper()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please choose from {', ' .join(valid_options)}")


size = get_proper_input("What size of the pizza do you want? S, M or L: ", ["S", "M", "L"])
pepperoni = get_proper_input("Do you want to add pepperoni? Y or N: ", ["Y", "N"])
extra_cheese = get_proper_input("Do you want to add extra cheese? Y or N: ", ["Y", "N"])

bill = 0

#switch is not in python but in 3.9v they introduced this match and case like alt to switch
match size:
    case "S":
        bill += 15
        if pepperoni == "Y":
            bill += 2
        if extra_cheese == "Y":
            bill += 1

    case "M":
        bill += 20
        if pepperoni == "Y":
            bill += 3
        if extra_cheese == "Y":
            bill += 1

    case "L":
        bill += 25
        if pepperoni == "Y":
            bill += 3
        if extra_cheese == "Y":
            bill += 1

    case _:
        print("Invalid pizza size selected.")

print("Your total bill: $"+str(bill))