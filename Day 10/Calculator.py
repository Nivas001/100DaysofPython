def asking(total):
    choose = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ")
    if choose == "y":
        getting_input(total)
    elif choose == "n":
        get_first_number()
    else:
        exit()

def get_first_number():
    first_no = float(input("What's your first number? "))
    getting_input(first_no)

def getting_input(first_no):
    operation = input("+\n-\n*\n/\nPick an operation: ")
    second_no = float(input("What's your second number? "))
    global tot

    match operation:
        case "+":
            tot = first_no + second_no
        case "-":
            tot = first_no - second_no
        case "*":
            tot = first_no * second_no
        case "/":
            tot = first_no / second_no

    print(f"{first_no} {operation} {second_no} = {tot}")
    asking(tot)

get_first_number()



