import random

randomNo = random.randint(1, 2)
if randomNo == 1:
    print("Head")
else:
    print("Tail")

friends = ["Gopal", "Pagal", "Vijay", "Dandapani", "Mithun"]
print(f"My friend {random.choice(friends)} will pay the bill today!!")