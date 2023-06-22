


import time
#warnings and instructions along with collection of name
print("the functions which this program can do are addition(sum),subtract(sub), divide(div), multiply(mult). please note the words written in brackets after the operation is the code word to be used to perform the function")
time.sleep(2)
name=input("Hello,Please enter you name: ")
print("WARNING!!!!!!! While subtracting please type the bigger number first and then the smaller number and for division please enter the dividend first the the divisor, other wise your answer will not be correct, thank you")
time.sleep(2)
#user enter numbers here
a= float( input("enter a number:"))
b= float( input("enter a second number number:"))
#type of function gets entered here
function=(input("what function would you like to perform:"))
#a small add on
print("Please wait while the computer calculates")
time.sleep(1)
print("Calculating")
time.sleep(3)
#declaring the functions
div=a/b 
mult=a*b
sum=a+b
sub=a-b 
#the real brains of this project
if function=="sum": 
    print("the sum is", sum)
    time.sleep(2)
    print("Thank you for using this calculator", name)
elif function!="sum " and function=="sub":
    print("the difference is ", sub)
    time.sleep(2)
    print("Thank you for using this calculator", name)
elif function!="sum " and function!="sub" and function=="mult":
    print("the product is ", mult)
    time.sleep(2)
    print("Thank you for using this calculator", name)
elif function!="sum " and function!="sub" and function!="mult" and function=="div":
    print("the quotient is ", div)
    time.sleep(2)
    print("Thank you for using this calculator,", name)    

