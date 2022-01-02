# Specifying the placeholder in the letter to a variable.
# Getting the names of people that we are going to send letters to.

PLACEHOLDER = "[name]"
names = open("./Input/Names/invited_names.txt", mode="r")
name_list = names.readlines()

# Getting the letter string.
letter = open("./Input/Letters/starting_letter.txt", mode="r")
starting_letter = letter.read()

# Putting the names in the letter, and creating a file for each letter.
for name in name_list:
    new_name = name.strip()
    final_letter = starting_letter.replace(PLACEHOLDER, new_name)
    file = open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w")
    file.write(final_letter)
