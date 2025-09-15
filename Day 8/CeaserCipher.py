
alphabet = ['a' , 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = ""
text = ""
shift = 0

def valid_option_check(prompt, valid_option):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_option:
            return user_input
        print(f"Please select from {',' .join(valid_option)} ")

def encrypt(org_message, shift):
    encrypted_word = ""
    for letter in org_message:
        if letter in alphabet:
            new_index = alphabet.index(letter) + shift
            encrypted_word += alphabet[new_index]
        else:
            encrypted_word += letter
    print("Your encrypted message: "+ encrypted_word)

def decrypt(org_message, shift):
    encrypted_word = ""
    for letter in org_message:
        if letter in alphabet:
            new_index = (alphabet.index(letter) - shift) % len(alphabet)
            encrypted_word += alphabet[new_index]
        else:
            encrypted_word += letter
    print("Your encrypted message: "+ encrypted_word)

def process_flow():
    global direction, text, shift
    direction = valid_option_check("Type 'encode' for encrypt, type 'decode' to decrypt: \n", ["encode", "decode"])
    text = input("Type your message:\n ").lower()
    shift = int(input("Type the shift number :\n"))

    if direction == "encode":
        encrypt(text, shift)
    if direction == "decode":
        decrypt(text, shift)

process_flow()




again = valid_option_check("Type 'yes' if you want to go again. Otherwise type 'no'.\n", ["yes", "no"])
if again == "yes":
    process_flow()
else:
    exit()
