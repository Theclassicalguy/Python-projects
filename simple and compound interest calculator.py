import time

def simple_interest():
    # Simple interest calculator
    p = float(input("Enter the principle amount:"))
    r = float(input("Enter the rate:"))
    t = float(input("Enter the time period:"))
    si = (p * r * t) / 100
    print("Calculating...")
    time.sleep(2)
    print("<-------------------------------------------------------->")
    print("The simple interest is:", si)
    print("<-------------------------------------------------------->")


def compound_interest():
    # Compound interest calculator
    print("<-------------------------------------------------------->")
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the rate: "))
    t = float(input("Enter the time period: "))
    n = float(input("Enter the frequency/number of times the interest is compounded annually: "))

    a = p * (1 + r/100/n)**(n*t)
    ci = a - p

    print("Calculating...")
    time.sleep(2)
    print("<-------------------------------------------------------->")
    print("The compound interest is:", ci)
    print(f"The amount is {a}")
    print("<-------------------------------------------------------->")


def main():
    # Welcome and interest calculating options
    print("<-------------------------------------------------------->")
    print("Welcome to the simple and compound interest calculator")
    print("<-------------------------------------------------------->")
    print("What function would you like to perform?")
    print("1. Simple Interest")
    print("2. Compound Interest")


def user_input():
    user_input = input("1 or 2? :")
    print("<-------------------------------------------------------->")
    if user_input == "1":
        simple_interest()
    elif user_input == "2":
        compound_interest()
    else:
        print("Invalid option, please try again")


main()
user_input()

  





