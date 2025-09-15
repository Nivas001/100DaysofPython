from datetime import date

def greet(name, location):
    print("Hello ", name)
    print(f"What is it like in {location}?")
    print(date.today())

#positional Argument 👇
greet("Angela", "London")

#keyword Argument 👇
greet(location="London", name="Nivas")