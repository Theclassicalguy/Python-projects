import random

choices=["rock","paper","scissors"]
computer_choice=random.choice(choices)
user_choice=input("Enter your choice (rock/paper/scissors):")

if user_choice.lower()==computer_choice :
    print("Your choice:",user_choice)
    print("Computers choice:",computer_choice)
    print("Its a tie") 

elif user_choice.lower()=="paper" and computer_choice=="rock" or user_choice.lower()=="scissors" and computer_choice=="paper" or   user_choice.lower()=="rock" and computer_choice=="scissors":
       print("Your choice:",user_choice)
       print("Computers choice:",computer_choice)
       print("You won!!")
       
else:print("Your choice:",user_choice); print("Computers choice:",computer_choice) ; print("You lost")
      

 