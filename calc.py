"A Simple Calculator"

from calc_art import LOGO

def addition(n1, n2):
    "Takes two values and returns their additions"
    return n1 + n2

def multiplication(n1, n2):
    "Takes two values and returns their multiplications"
    return n1 * n2

def subtraction(n1, n2):
    "Returns the subtraction of two values"

def division(n1, n2):
    "Returns the division given the division is not zero"
    if n2 == 0:
        return
    return n1 /n2

def simple_calculator():
    "A simple iterative Calculator."
    continue_calculation = True
    value1 = 0
    setval1 = True

    while continue_calculation:

        if setval1:
            value1 = float(input("What is your first value ?: "))

        operator = input("Pick an operation:\n\t+\n\t-\n\t/\n\t*\t: ")
        value2 = float(input("What is your Second value ?: "))
        
        if operator == "/" and (value2 == 0.0):
            value2 = float(input("Selecting 0.0 as your divisor will result in a Zero divion error, input another value that isn't Zero: "))

        calculator = {"+": addition(value1, value2), "-": subtraction(value1, value2), "*": multiplication(value1, value2), "/": division(value1, value2)}

        calculation = calculator[operator]

        print(f"{value1} {operator} {value2} = {calculation}")

        user_choice = input(f"Type 'y' to continue calculating with {calculation}, 'n' to start new calculation and 'q' to quit: ").lower()

        if user_choice == 'y':
            value1 = calculation
            setval1 = False
            continue
        elif user_choice == 'n':
            continue
        elif user_choice == 'q':
            print("Bye!")
            continue_calculation = False

print(LOGO)
simple_calculator()
