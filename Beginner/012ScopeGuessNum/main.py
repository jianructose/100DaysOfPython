#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
from replit import clear
ans = random.randint(1, 100)


def play():
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100 inclusive.\nChoose a difficulty. ")
  level = input("Type 'easy' or 'hard': \n")
  if level[0] == "e":
    n_attempts = 10
  else:
    n_attempts = 5

  while n_attempts > 0:
    print(f"You have {n_attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    n_attempts-=1
    if guess > ans:
      print(f"Too high.\nGuess again.")
    elif guess == ans:
      print("Yes, you got it!!😸")
      n_attempts = 0
    else:
      print("Too low. \nGuess again.")

  print("You lose 😥")

while input("Start the game? 'y' or 'n'\n") == 'y':
  clear()
  play()

  