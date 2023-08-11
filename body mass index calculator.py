import time
import webbrowser

print("<-------------------------------------------------------->")
weight=float(input("Enter your weight in kilograms:"))
print("<-------------------------------------------------------->")
height=float(input("Enter your height in centimeters:"))
bmi=(weight/height/height)*10000
print("<-------------------------------------------------------->")
print("Your BMI is, ",bmi)
if bmi<18.5:
    print("You are underweight.")
    print("<-------------------------------------------------------->")
    print("To know more about BMI click this link : ",input("Press enter to open the link."),  webbrowser.open("https://www.wikiwand.com/en/Body_mass_index"))
elif bmi>18.5 and bmi<24.9:
    print("You have a normal weight")
    print("<-------------------------------------------------------->")
    print("To know more about BMI click this link : ",input("Press enter to open the link."), webbrowser.open("https://www.wikiwand.com/en/Body_mass_index"))
elif bmi>25 and bmi<29.9:
    print("Your are overweight")
    print("<-------------------------------------------------------->")
    print("To know more about BMI click this link : ",input("Press enter to open the link."),  webbrowser.open("https://www.wikiwand.com/en/Body_mass_index"))
elif bmi>=30:
    print("You are obese")
    print("<-------------------------------------------------------->")
    print("To know more about BMI click this link : ",input("Press enter to open the link."),  webbrowser.open("https://www.wikiwand.com/en/Body_mass_index"))