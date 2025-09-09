import random
from colorama import Fore, Style

print ( Fore.RED+ r"""


      ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █           
     ▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █           
     ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒          
     ░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒          
     ░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░          
      ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒           
      ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░          
      ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░           
      ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░           

""" + Style.RESET_ALL)



Hangman_pics = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print("WELCOME TO HANGMAN GAME!!!")

user_life = 0

list_of_words = [
    "apple", "book", "desk", "pen", "cat", "dog", "tree", "house", "car", "phone",
    "computer", "laptop", "keyboard", "mouse", "chair", "table", "door", "window",
    "wall", "floor", "bottle", "camera", "clock", "flower", "glass", "hat", "jacket",
    "lamp", "mirror", "notebook", "pencil", "plant", "shirt", "shoe", "stove",
    "watch", "bed", "cup", "bike", "phone", "road", "river", "cloud", "plane",
    "train", "boat", "beach", "mountain", "forest", "star", "moon"
]

random_word = random.choice(list_of_words)
#print(random_word)
len_random_word = len(random_word)
guess_letter = []

while user_life <= 7:
    dashes = ""
    for char in random_word:
        if char in guess_letter:
            dashes += char
        else:
            dashes += "_"
    print(f"The letter contains: "+ dashes +f". Still {len_random_word} letters remaining to find")
    letter = input("Guess the letter🔎 : ")
    if letter in random_word:
        len_random_word -= 1
        guess_letter.append(letter)
        if set(random_word) .issubset(set(guess_letter)):
            print(f"Congratulation you found the word {random_word}")
            break
        continue
    else:
        user_life += 1
        if user_life >= 7:
            print("You ran out life 😵")
            print(f"The word is {random_word}")
            break
        print(Hangman_pics[user_life - 1])
        print(f"Your remaining life : {7 - user_life}")



