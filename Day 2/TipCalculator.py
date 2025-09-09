print("Welcome to our Kadai!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
persons = int(input("How many people to split the bill? "))

total_bill = (bill * tip/100) + bill
each_person_bill = round(total_bill/ persons, 2)
print(f"Each person should pay: ${each_person_bill}")