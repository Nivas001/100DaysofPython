



def calculate_love_score(fir_person, sec_person):
    # global for a variable can only be set inside a function not for creating an idea one.
    true_score = 0
    love_score = 0
    for letter in fir_person + sec_person:
        if letter in "TRUE":
            true_score += 1

        if letter in "LOVE":
            love_score += 1

    print(f"{true_score}{love_score}")

calculate_love_score("Wafiq".upper(), "laaracraft".upper())