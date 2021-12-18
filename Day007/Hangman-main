##Importing necessary elements to write the game.
import random
from hangman_words import word_list 
from hangman_art import logo 
from hangman_art import stages
from replit import clear

## Selecting a random word from the list of words in word_list
chosen_word = random.choice(word_list)

## Defining the amount of lives,list to store previous guesses, and the end_of_game variable.

word_length = len(chosen_word)
end_of_game = False
lives = 6
previous_guesses = []

## Hangman art logo
print(f"Welcome to the hangman game!\n{logo}")

## Creating a blank list as long as the word's length with "_" characters to print out so user can see his/her progress during the game.
display = []
for _ in range(word_length):
    display += "_"

## Creating a While loop to repeat asking the user for letters as long as  end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
## Writing the guesses to previous_guesses list if it's not already there. If it's there, prints a warning message to user that the guess is previously entered.
    if guess not in previous_guesses:
      previous_guesses.append(guess)
    else:
      print(f"You have already  guessed {guess} before. Try another guess.")
## Checking if the guessed letter is in the word, and replacing the "_" character in the list displayed to user with the letter guessed if the letter is guessed correctly. 
      for i in range(word_length):
        if chosen_word[i] == guess:
          display[i] = guess

## If guessed incorrectly, prints a warning messsage that the user lost a life and decreases lives variable by 1. When lives reach to 0, the game ends.
        else:
          print(f"The letter {guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

## Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

## Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

## Print the stage of the hangman for better user experience.
    print(stages[lives])
