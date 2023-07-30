
# Importing time module
import time
calculation_history=[]

#declaring functions
def add():
    print("<----------------------------------------------------------------------------->")
    # User enters numbers here
    a = float(input("Enter a number: "))
    print("<----------------------------------------------------------------------------->")
    b = float(input("Enter a second number: "))
    
    sum=a+b

    # a small add on
    print("<----------------------------------------------------------------------------->")
    print("Please wait while the computer calculates")
    time.sleep(1)
    print("Calculating")
    time.sleep(3)
    print("<----------------------------------------------------------------------------->")

    print("The sum is", sum)
    calculation_history.append(f"{a} + {b} = {sum}")

def sub():
     print("<----------------------------------------------------------------------------->")
     a = float(input("Enter a number: "))
     print("<----------------------------------------------------------------------------->")
     b = float(input("Enter a second number: "))
     
     sub=a-b

     print("<----------------------------------------------------------------------------->")
     print("Please wait while the computer calculates")
     time.sleep(1)
     print("Calculating")
     time.sleep(3)
     print("<----------------------------------------------------------------------------->")

     print("The difference is", sub)  
     calculation_history.append(f"{a} - {b} = {sub}") 

def div():
    print("<----------------------------------------------------------------------------->")
    a = float(input("Enter the numerator: "))
    print("<----------------------------------------------------------------------------->")
    b = float(input("Enter the denominator: "))
    
    div=a/b

    print("<----------------------------------------------------------------------------->")
    print("Please wait while the computer calculates")
    time.sleep(1)   
    print("Calculating")
    time.sleep(3)
    print("<----------------------------------------------------------------------------->")

    print("The qoutient is", div)    
    calculation_history.append(f"{a} / {b} = {div}")

def mult():
     print("<----------------------------------------------------------------------------->")
     a = float(input("Enter a number: "))
     print("<----------------------------------------------------------------------------->")
     b = float(input("Enter a second number: "))
     
     mult=a*b

     print("<----------------------------------------------------------------------------->")
     print("Please wait while the computer calculates")
     time.sleep(1)
     print("Calculating")
     time.sleep(3)
     print("<----------------------------------------------------------------------------->")

     print("The product is", mult)    
     calculation_history.append(f"{a} * {b} = {mult}")

def sqrt():
    print("<----------------------------------------------------------------------------->")
    a = float(input("Enter the number you want to find the square root of: "))
    sqroot=a**0.5

    print("<----------------------------------------------------------------------------->")
    print("Please wait while the computer calculates")
    time.sleep(1)
    print("Calculating")
    time.sleep(3)
    print("<----------------------------------------------------------------------------->")

    print(f"The square root of {a} is {sqroot} ")
    calculation_history.append(f"√{a} = {sqroot}")

def c_root():
    print("<----------------------------------------------------------------------------->")
    a = float(input("Enter the number you want to find the cube root of: "))
    croot=a**(1/3)

    print("<----------------------------------------------------------------------------->")
    print("Please wait while the computer calculates")
    time.sleep(1)
    print("Calculating")
    time.sleep(3)
    print("<----------------------------------------------------------------------------->")

    print(f"Thw cube root{a} is {croot} ")
    calculation_history.append(f"∛{a} = {croot}")

def expt():
    print("<----------------------------------------------------------------------------->")
    a = float(input("Enter the base number: "))
    b = float(input("Enter the exponent:"))
    exponent=a**b
    print("<----------------------------------------------------------------------------->")
    print("Please wait while the computer calculates")
    time.sleep(1)
    print("Calculating")
    time.sleep(3)
    print("<----------------------------------------------------------------------------->")

    print(f"{a} raised to the power of {b} = {exponent} ")
    calculation_history.append(f"{a} ^ {b} = {exponent}")    

   
def main():  #this is the main function
 
    # Welcome with getting user name
    print("Welcome to Python Calculator")
    time.sleep(1)
    global name
    name = input("Hello, please enter your name: ")
    time.sleep(1)
    user_option()
       
def user_option():  #this function gives the user options for functions
     print("<----------------------------------------------------------------------------->")
     print("1. Perform a calculation")
     print("2. View calculation history")
     print("3. Exit")
     user_option=input("Enter your choice (1/2/3):")

     if user_option=="1":
        calculations()

     elif user_option=="2":
        display_calc_history()

     elif user_option=="3":
         print(f"Thank you for using this calculator, {name}")   

     else:
         print("Invalid function entered") 
    

def display_calc_history():
    print("<----------------------------------------------------------------------------->")
    print("Loading calculations history.........")
    time.sleep(2)
    print("Calculations history:")
    #using a for loop to print all the items is calculations_history list with numbering
    for i, calculations in enumerate(calculation_history, start=1):
        print(f"{i}. {calculations}")
    user_option()


def calculations():  #this function does the calculations
    print("Welcome!!")
    time.sleep(1)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square root")
    print("6. Cube root")
    print("7. Exponentation")
    print("<----------------------------------------------------------------------------->")
    
    # Type of function gets entered here
    function = input("What function would you like to perform (1/2/3/4/5/6/7): ")
    
    
    
    #real brains of this project
    if function == "1":
        add()
    elif function == "2":
        sub()
    elif function == "3":
        mult()
    elif function == "4":
        div()
    elif function=="5":
        sqrt()    
    elif function=="6":
        c_root()
    elif function=="7":
        expt()    
    else:
        print("Invalid function entered!")

    user_option()    

  

main()
