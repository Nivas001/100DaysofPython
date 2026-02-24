import random

def giving_random_number():
    my_card1 = random.randint(1, 11)
    my_card2 = random.randint(1, 11)
    print(f"Your cards : [{my_card1}, {my_card2}]")

    comp_card1 = random.randint(1, 11)

    print(f"Computer's first card: ", comp_card1)

    tot = my_card1+ my_card2

    if tot == 21:
        add_card(tot, comp_card1)

    option1 = input("Type 'd' for double or type any other letter for hit or pass : ")
    if option1 == "d":
        tot += tot
        print(f"Your score: {tot}")
        add_comp_card(tot, comp_card1)
    else:
        ask_for_card(tot, comp_card1)

def add_comp_card(total, total1):
    if 17 == total1:
        choose = round(random.random(), 1)
        # making 70% chance that if the comp card comes 17 to 19 the computer will hit and 30% stand
        if choose < 0.7:
            add_card(total, total1)
        else:
            calculate_who_won(total, total1)

    elif 18 <= total1:
        calculate_who_won(total, total1)

    elif total1 < 17:
        add_card(total, total1)


def add_card(total, total1):
    comp_card4 = random.randint(1, 11)
    print("Computer takes a card (HITS) : ", comp_card4)
    total1 += comp_card4
    print("Computer's total now: ", total1)
    add_comp_card(total, total1)


def calculate_who_won(total, total1):
    print(f"Your Score: {total} and Computer's score: {total1}")

    if total > 21 and total1 > 21:
        print("Both Busted!, So match draw")

    elif total > 21 > total1:
        print("You're Busted!, Computer wins")

    elif total1 > 21 > total:
        print("Computer Busted!, You wins")

    else:
        if total > total1:
            print("You won the game!!")
        else:
            print("Computer Won! You Lose")


def ask_for_card(total, total1):
    option = input("Type 'y' to get another card, type 'n' to pass : ")
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
    elif option == "n":
        print(f"Your score {total}")
        add_comp_card(total, total1)



giving_random_number()