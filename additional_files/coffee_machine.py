"""A simple coffee machine logic."""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

WATER = resources["water"]
MILK = resources["milk"]
COFFEE = resources["coffee"]
MONEY = 0

def print_report():
    """Print's out a report of the current
    inventory of the resources."""
    print(f"\tWater: {WATER}ml\n\tMilk: {MILK}ml\n\tCoffee: {COFFEE}g\n\tMoney: ${MONEY}")


def calculate_cost(type_of_drink):
    global MONEY, WATER, MILK, COFFEE
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))
    total_cost = (quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01)
    total_cost = round(total_cost, 2)
    cost_of_drink = MENU[type_of_drink]["cost"]

    if total_cost < cost_of_drink:
        print("Sorry that's not enough money. Money refunded.")
    if total_cost > cost_of_drink:
        MONEY += cost_of_drink
        if type_of_drink != "espresso":
            MILK -= MENU[type_of_drink]["ingredients"]["milk"]
        WATER -= MENU[type_of_drink]["ingredients"]["water"]
        COFFEE -= MENU[type_of_drink]["ingredients"]["coffee"]
        print(f"Here is ${total_cost - cost_of_drink} in change.")
        print(f"Here is your {type_of_drink}. Enjoy!")


while True:
    user_drink_pref = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_drink_pref == "espresso" or user_drink_pref == "latte" or user_drink_pref == "cappuccino":
        if user_drink_pref == "espresso":
            if WATER < MENU["espresso"]["ingredients"]["water"]:
                print("Sorry, there is not enough water!")
            else:
                calculate_cost("espresso")
        if user_drink_pref == "latte":
            if WATER < MENU["latte"]["ingredients"]["water"]:
                print("Sorry, there is not enough water!")
            else:
                calculate_cost("latte")
        if user_drink_pref == "cappuccino":
            if WATER < MENU["cappuccino"]["ingredients"]["water"]:
                print("Sorry, there is not enough water!")
            else:
                calculate_cost("cappuccino")
    elif user_drink_pref == "off":
        print("Turning off.........")
        break
    elif user_drink_pref == "report":
        print_report()
    else:
        print("Kindly input a valid choice.")


# TODO 1: Ask the user what they would like
# TODO 2: "off" should prompt the coffee machine to turn off
# TODO 3: "report" should show the current resource values
# declare the water, milk, coffee as global values
# create a function that returns the well organised, print statement
# TODO 4: According to the user's choice of drink, check whether there are enough resources, print out the resource missing
# use a function that takes an int as a value, the value of the int is the position of the item in question in the menu list.
# TODO 5: Process the coins to find their value quarter = 0.25 dime = 0.10 nickle = 0.05 penny = 0.01
# also create a function for this
# TODO 6: According to user's money check whether if it is enough.
# works in hand with todo 5, achievable
# TODO 7: Make coffee if the right requirements are met.
