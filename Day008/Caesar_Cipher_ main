## Function to perform encrypt and decrypt actions.
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      while new_position > len(alphabet):
        new_position = new_position % len(alphabet)
      while new_position < 0:
        new_position += len(alphabet)
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")
## Importing and printing ascii logo of the program.
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
## Getting inputs such as direction(encode or decode), shift amount, and the message to be encode/decode in a while loop, 
allowing program to continue as long as user types yes to repeat. Function is called in while loop with arguments assigned to parameters.
repeat = "yes"
while repeat == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  repeat = input("Type 'yes' if you want to go again.")
if repeat != "yes":
  print("Goodbye!")
  
