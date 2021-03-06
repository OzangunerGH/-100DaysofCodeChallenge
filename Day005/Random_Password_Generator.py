import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")

## Asking for the amount of characters for password to contain by each character type(alphebetical,symbols,numeric)  
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
##Creating a list variable to store the x amount of (where X is inputted by user for each character type) random characters from the corresponding lists. 
password_list = []
##Creating a string variable to print the final password.
password = ""
## Creating for loops to store random characters from the main lists by the amount inputted by user.
for i in range(0, nr_letters):
  password_list += letters[(random.randint(0,51))] 
for i in range(0, nr_symbols):
  password_list += symbols[random.randint(0,8)]
for i in range(0, nr_numbers):
  password_list += numbers[random.randint(0,9)]
  
## Shuffling the list so the order of the characters are random.
random.shuffle(password_list)

## Writing the elements of the list into a string to print the final password.
for i in range(0, len(password_list)):
  password += password_list[i]
print(f"Your password is: {password}")
