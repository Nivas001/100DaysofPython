from datetime import datetime

def life_in_weeks(age):
    #weeks = (90 * 52) - (age * 52)
    print(f"You have {(90 - age) * 52} weeks left.")

life_in_weeks(56)