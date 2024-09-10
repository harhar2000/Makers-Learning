#Loop
    # Ask: roll the dice?
    # If user enters y
    #   Generate two random numbers
    #   Print them
    # If user enters n
    #   Print thank you message
    #   Terminate
    # Else:
    #   Print invalid choice

import random

while True:
    choice = input("Roll the Dice?:  ").lower()
    if choice == "n":
        print("Thanks for playing")
        break
    elif choice == "y":
        die1 = random.randint(0,6)
        die2 = random.randint(0,6)
        print(f"({die1}, {die2})")
    elif choice != "y":
        print("Invalid choice!")