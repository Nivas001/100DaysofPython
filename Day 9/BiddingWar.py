from colorama import Fore, Style


print(Style.BRIGHT + Fore.YELLOW + "!!Let's start bidding wars!!".center(160) + Style.BRIGHT + Fore.YELLOW )

def calculate():
    highest_bidder = max(bids, key=bids.get)
    highest_bid = bids[highest_bidder]

    print(f"\nThe winner is {highest_bidder} with a {highest_bid}")

bids = {}
def asking_participants():

    name = input("What's your name? ")
    price = int(input("Bid your price? "))

    bids[name] = price

    follow = input("Is there any other bidder? ")
    if follow == "yes":
        asking_participants()
    else:
        calculate()

asking_participants()



