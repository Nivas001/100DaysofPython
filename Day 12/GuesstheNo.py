import random

attempt = 0

def printing():
    print("Welcome to the Number Guessing Game!")
    no = random.randint(1, 100)

    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    global attempt
    if difficulty == "easy":
        attempt = 10
    elif difficulty == "hard":
        attempt = 5
    else:
        printing()

    finding_no(no)


def finding_no(no):
    global attempt

    if attempt>0:
        guess = int(input("Make a guess: "))

        if guess == no:
            print(f"You got it! The answer was {no}")

        elif guess > no:
            print("Too High. \nGuess again.")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")
            finding_no(no)

        elif guess < no:
            print("Too Low. \nGuess again.")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")
            finding_no(no)

        else:
            print("IDK, what's wrong in code or game!!!!")

    else:
        print(f"You are out of lives. You didn't find the number, the number was {no}.")

printing()