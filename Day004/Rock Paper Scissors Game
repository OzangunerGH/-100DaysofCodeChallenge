## Rock paper scissors game in Python
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
#Getting users choice
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
#Converting user's choice to integer
user_choice = int(user_choice)
## Getting a randomized computer choice
computer_choice = random.randint(0,2) 
## Creating a list to print what the user's and computer's choices.
rps =[rock,paper,scissors]

## Defining win-draw-lose conditions.
if (computer_choice == user_choice):
  print(f"Computer Chose:\n\n{rps[computer_choice]}\nYou Chose:\n\n{rps[user_choice]}\nIt is a draw.")
elif (user_choice == 2) and (computer_choice == 1):
  print(f"Computer Chose:\n\n{rps[computer_choice]}\nYou Chose:\n\n{rps[user_choice]}\nYou win!")
elif (user_choice == 1) and (computer_choice == 0):
   print(f"Computer Chose:\n\n{rps[computer_choice]}\nYou Chose:\n\n{rps[user_choice]}\nYou win!")
elif (user_choice == 0) and (computer_choice == 2):
   print(f"Computer Chose:\n\n{rps[computer_choice]}\nYou Chose:\n\n{rps[user_choice]}\nYou win!")
elif (user_choice == 1) and (computer_choice == 2):
  print(f"Computer Chose:\n\n{rps[computer_choice]}\nYou Chose:\n\n{rps[user_choice]}\nYou lose.")
elif (user_choice == 0) and (computer_choice == 1):
   print(f"Computer Chose:\n\n{rps[computer_choice]}\nYou Chose:\n\n{rps[user_choice]}\nYou lose.")
elif (user_choice == 2) and (computer_choice == 0):
   print(f"Computer Chose:\n\n{rps[computer_choice]}\nYou Chose:\n\n{rps[user_choice]}\nYou lose.")
   ## Wrong entry condition.
else:
  print("Wrong entry. Try again later.")
