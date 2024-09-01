# The provided script allows a user to play two games consecutively:

# A Number Guessing Game.
# A Quiz.
# Currently, the code is structured in a procedural way, with all functionality exposed at the top level.

# Your task is to encapsulate the code:

# Decide:

    # How many classes should be created.
    # What their names should be.
    # Which state and behaviour should be encapsulated within each class.
    # Create the classes:

# Implement the code in an object-oriented manner.
# Consider access modifiers and decide what state/behaviour should be private or protected.
# Note: You are only required to create the classes. The script should maintain its current functionality after the refactoring.



from random import *

print("First we'll play a guessing game, then we'll do a quiz!")
input("Press return to start")
currentNumber = Random().randint(1, 10)
playerName = input("what is your name?")
playerGuess = input("Please guess a number between 1 and 10 (inclusive)")
while int(playerGuess) != currentNumber:
  print(f"Nope, try again {playerName}!")
  playerGuess = input("Please guess a number between 1 and 10 (inclusive)")
print(f"Well done {playerName}, you guessed {playerGuess}, which was correct")

# a quiz / puzzle platform
# quiz class
# puzzle class

print("OK well done, now it's quiz time")
input("Press return to start")

playerScore = 0

answer1 = input("What is the capital Greenland?")
if answer1 == "Nuuk":
  print("correct, you scored 1pt")
  playerScore += 1
else:
  print("incorrect - nil points!")


answer2 = input("What is the largest planet in our Solar System?")
if answer2 == "Jupiter":
    print("correct, you scored 1pt")
    playerScore += 1
else:
    print("incorrect - nil points!")


answer3 = input("Who wrote the play 'Romeo and Juliet'?")
if answer3 == "William Shakespeare":
    print("correct, you scored 1pt")
    playerScore += 1
else:
    print("incorrect - nil points!")


answer4 = input("What is the chemical symbol for gold?")
if answer4 == "Au":
    print("correct, you scored 1pt")
    playerScore += 1
else:
    print("incorrect - nil points!")


answer5 = input("In which year did the Titanic sink?")
if answer5 == "1912":
    print("correct, you scored 1pt")
    playerScore += 1
else:
    print("incorrect - nil points!")

print(f"You scored {playerScore}")




# ===========================================================================



# from random import *

# class GuessingGame:
#    def __init__(self):
#       self.currentNumber = randint(1, 10)
#       self.playerName = ""

#    def start_game(self):
#       print("First we'll play a guessing game, then we'll do a quiz!")
#       input("Press return to start")
#       self.playerName = input("what is your name? ")
#       playerGuess = int(input("Please guess a number between 1 and 10 (inclusive): "))

      
#       while int(playerGuess) != self.currentNumber:
#         print(f"Nope, try again {self.playerName}!")
#         playerGuess = int(input("Please guess a number between 1 and 10 (inclusive): "))
#       print(f"Well done {self.playerName}, you guessed {playerGuess}, which was correct")
      


# class Quiz:
#    def __init__(self):
#       self.playerScore = 0
      
#    def start_quiz(self):
#       print("OK well done, now it's quiz time")
#       input("Press return to start")

#       answer1 = input("What is the capital Greenland? ")
#       if answer1 == "Nuuk":
#        print("correct, you scored 1pt")
#        self.playerScore += 1
#       else:
#         print("incorrect - nil points!")
 

#       answer2 = input("What is the largest planet in our Solar System? ")
#       if answer2 == "Jupiter":
#           print("correct, you scored 1pt")
#           self.playerScore += 1
#       else:
#           print("incorrect - nil points!")


#       answer3 = input("Who wrote the play 'Romeo and Juliet'? ")
#       if answer3 == "William Shakespeare":
#           print("correct, you scored 1pt")
#           self.playerScore += 1
#       else:
#           print("incorrect - nil points!")


#       answer4 = input("What is the chemical symbol for gold? ")
#       if answer4 == "Au":
#           print("correct, you scored 1pt")
#           self.playerScore += 1
#       else:
#           print("incorrect - nil points!")


#       answer5 = input("In which year did the Titanic sink? ")
#       if answer5 == "1912":
#           print("correct, you scored 1pt")
#           self.playerScore += 1
#       else:
#           print("incorrect - nil points!")

#       print(f"You scored {self.playerScore}")

# guessing_game = GuessingGame()
# guessing_game.start_game()

# quiz = Quiz()
# quiz.start_quiz()