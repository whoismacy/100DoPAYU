"A simple bidding program"
import os

from bid_art import LOGO

print(LOGO)
bidders = {}
CONT = True

while CONT:
    TEMP_VALUE = 0
    TEMP_KEY = None
    name = input("What is your name? ")
    bid_price = float(input("What is your bid price ? $"))
    bidders[name] = bid_price
    other = input("Are there any other bidders 'yes' or 'no' ? ").lower()

    if other == "yes":
        os.system("clear")
        print(LOGO)
        continue
    else:
        CONT = False

        for key, value in bidders.items():
            if bidders[key] > TEMP_VALUE:
                TEMP_VALUE = bidders[key]
                TEMP_KEY = key

        print(f"The Winner of the Bid is {TEMP_KEY} with a bid of ${TEMP_VALUE}")
