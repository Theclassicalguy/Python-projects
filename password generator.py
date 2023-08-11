import random
import pyperclip


dict1="abcdefghijklmnopqrstuvwxyz"
dict2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dict3="1234567890"
dict4="!@#$%^&*(){}[]_-:;"

all_characters=dict1+dict2+dict3+dict4

password="".join(random.choices(all_characters, k=max(14, random.randint(1,25))))

print("The password is:", password)

user_input=input("Would you like to copy the password to clipboard? (Y/N)")
if user_input.lower()=="y":
    pyperclip.copy(password)
    print("The password has been copied")

else:print("Thank you for using this password generator")



