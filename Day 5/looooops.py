student_score = [150, 225, 124, 168, 125, 908, 254, 301, 205, 154, 251, 301, 321, 210, 512, 823]


big_no = 0;
for score in student_score:
    if score > big_no:
        big_no = score

print(big_no)

#going to print total from 1 to 100 incl both
total = 0
for number in range(1, 101):
    total += number

print(total)

for no in range(1, 101):
    if no%5 == 0 and no%3 == 0:
        print("FizzBuzz")
    elif no%3 == 0:
        print("Fizz")
    elif no%5 == 0:
        print("Buzz")
    else:
        print (no)