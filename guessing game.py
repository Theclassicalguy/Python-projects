import random

def guessing_game():
    target_number=random.randint(1,100)
    attempts=0

    while True:
        guess=int(input("Guess the number between 1 to 100:"))
        attempts+=1

        if guess <target_number:
            print("Too low! Please try again.")
            print("<------------------------------------------>")
        elif guess>target_number:
            print("Too high! Please try again")
            print("<------------------------------------------>")
        else:
            print(f"Congratulations you've guessed the number in {attempts} attempts")
            break

guessing_game()