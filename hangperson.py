#hangman.py
# A program about hanging people if you don't spell things correctly.

from random import randint

words = ["test"]
numWrong = 0
listedWord = [None]

# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over.
def hangperson():
   global listedWord

   # Greet the user
   print("Let's play a game of hangperson!")

   # Randomly select a word from the list of words
   word = words[randint(0,len(words)-1)]

   # Make the randomly selected word into a list object
   listedWord = list(word)

   # Make another list the same length as the word, but with 
   # '_' instead of letters. This will track the user's progress.
   # Use the variable name currentState
   currentState = ["_"] * len(word)

   # Print the initial state of the game
   printHangperson(currentState)

   # Start the game! Loop until the user either wins or loses
   while currentState != listedWord and numWrong < 6:
      guess = userGuess()
      currentState = updateState(guess, currentState)
      printHangperson(currentState)

   # Determine if the user won or lost, and then tell them accordingly
   if numWrong >= 6:
      print("Oh no! The person hung. You lost :(")
      exit()
   else:
      print("You did it! The person didn't hang! Congrats.")
      exit()


# This helpful function prompts the user for a guess, 
# accepting only single letters.
# DO NOT CHANGE
#
# returns a letter
def userGuess():
   guess = input("Guess a letter in the word! (Say 'exit' to stop playing) ")
   while len(guess) != 1:
      if guess == "exit":
         exit()
      elif len(guess) != 1:
         print("You must guess only ONE letter.")
         guess = input("Try again.")

   return guess


# Update the state of the game based on the user's guess.
#
# guess: a character guessed by the user
# currentState: the current state of the word/game
#
# return currentState
def updateState(guess, currentState):
   global numWrong

   # First, determine if the letter guessed is in the word.
   # If it isn't, tell the user and update the numWrong var
   # If it is, congratulate them and update the state of the game.
   #    To update the state, make sure to replace ALL the '_' with
   #    the guessed letter.
   numInWord = listedWord.count(guess)

   if numInWord == 0:
      print("Oh no! There's no", guess, "in the word!")
      numWrong += 1
   else:
      print("Woohoo! There are",numInWord,guess,"in the word!")
      for i in range(len(listedWord)):
         if listedWord[i] == guess:
            currentState[i] = guess

   return currentState


# A helpful function to print the hangman.
# DO NOT CHANGE
#
# state: current state of the word
def printHangperson(state):
   person = [" O "," | \n | ", "\| \n | ", "\|/\n | ", "\|/\n | \n/  ", "\|/\n | \n/ \\"]
   print()

   if numWrong > 0:
      print(person[0])

   if numWrong > 1:
      print(person[numWrong-1])

   print("\n\n")

   for i in state:
      print(i, end=" ")

   print("\n")

# This line runs the program on import of the module
hangperson()