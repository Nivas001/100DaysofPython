import random

def giving_random_number():
    my_card1 = random.randint(1, 11)
    my_card2 = random.randint(1, 11)
    print(f"Your cards : [{my_card1}, {my_card2}]")

    comp_card1 = random.randint(1, 11)
    comp_card2 = random.randint(1, 11)
    print(f"Computer's first card: ", comp_card1)

    tot = my_card1+ my_card2
    tot1 = comp_card1 + comp_card2

    ask_for_card(tot, tot1)

def add_comp_card(total, total1):
    if total > 21:
        print("You lose, Computer won")
    elif 17 < total1 < 21:
        print(f"Your Score: {total} and Computer's score: {total1}")
        if total > total1:
            print("You won")
        else:
            print("Computer won")
    elif total1 < 17:
        comp_card3 = random.randint(1, 11)
        print("Computer takes a card (HITS) : ", comp_card3)
        total1 += comp_card3
        print("Computer's total now: ", total1)
        add_comp_card(total, total1)
    elif total1 > 21:
        print("You won, Computer is busted")



def ask_for_card(total, total1):
    option = input("Type 'y' to get another card, type 'n' to pass: ")
    if option == "y":
        my_card3 = random.randint(1, 11)
        print("Your card : ",my_card3)
        total += my_card3
        print("Your updated score: ", total)
        print("Computer's score: ", total1)

        if total > 21:
            add_comp_card(total, total1)
        else:
            ask_for_card(total, total1)
    if option == "n":
        add_comp_card(total, total1)



giving_random_number()