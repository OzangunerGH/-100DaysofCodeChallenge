import pandas
# Reading CSV Data to create DataFrame
df = pandas.read_csv("nato_phonetic_alphabet.csv")
# Creating a dictionary of Letter:Word from the DataFrame
new_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# Asking User to input a word
user_input = input("Enter a word you would like to spell with words.").upper()
# Creating a list of letters from the string user input.
user_input_letters = [letter for letter in user_input]
# Iterating the list through dictionary to get the right words for the letters in the list to a new list.
word_list = [value for (key, value) in new_dict.items() if key in user_input_letters]
print(word_list)
