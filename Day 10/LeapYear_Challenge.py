

def is_leap_year(year):
    if year == "":
        return "Please type proper year!!"

    return (year %4==0 and year%100 != 0) or (year%400 == 0)

choice = is_leap_year(2024)
print(choice)