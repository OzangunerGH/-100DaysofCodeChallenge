## Importing necessary functions and logo.
import random
from art import logo
from replit import clear
def difficulty():
  """This function allows user to select a difficulty, and based on the choice user gets the corresponding number of attempts"""
  attempts = 5
  difficulty = input("Select game difficulty. Type 'hard' for hard type 'easy' for easy\n").lower()
  if difficulty == "easy":
    attempts += 5
  print(f"You have {attempts} guesses.")
  return attempts
def check_answer(guess,answer,lives):
    """This function compares if the number guessed is equal to the answer and prints out the result and number of attempts left."""
  global game_ended
  if guess == answer:
    print("Congratulations. Your guess is correct!")
    game_ended = True
  elif guess > answer:
    print(f"{guess} is too high.You have {lives-1} guesses left.")
    return lives -1
  elif guess < answer:
    print(f"{guess} is too low. You have {lives-1} guesses left.")
    return lives-1
repeat = True
## This is the main code block of the guessing game. 
while repeat:
  game_ended = False
  clear()
  answer = random.randint(1,100)
  print(logo)
  print("Welcome to the Number Guessing Game!\n")
  lives = difficulty()
  print("I'm thinking of a number between 1 and 100.Type your guess.\n")
  while game_ended == False and lives > 0:
    guess = int(input("Guess a number between 1 and 100."))
    lives = check_answer(guess,answer,lives)
  another_game = input("Do you want to play again?\n Type y for yes, n for no.\n")
  if another_game == "n":
    clear()
    repeat = False
    


