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
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "n":
        print("Thanks for playing!")
        break
    elif choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"You rolled: {die1} and {die2}")
    else:
        print("Invalid choice!")



