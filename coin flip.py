import random

def coin_flip():
    flip=random.choice(["Heads", "Tails"])
    print(f"The coin landed on:{flip}")
coin_flip()
