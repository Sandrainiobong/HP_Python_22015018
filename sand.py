import random

while True:
    action = input("Enter toss to through a dice or quit to end: ")
    if action == "toss":
        dice = random.randint(1,6)
        print("Dice roll is:", dice)
    elif action == "quit":
        break
    else:
        print("wrong input,pleaae try again.")