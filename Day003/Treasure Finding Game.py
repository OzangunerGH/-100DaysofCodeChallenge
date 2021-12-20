first_input = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right'").lower()
if first_input == "left":
  second_input = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n").lower()
  if second_input != "wait":
    print("You made an invalid choice. Game Over!")
  else:
    third_input = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?").lower()
    if third_input == "red":
      print("Its a room full of fire. Game Over!")
    elif third_input == "blue":
      print("You found the treasure! You win!")
    elif third_input == "yellow":
      print("You enter a room full of beasts. Game Over!")
    else:
      print("You choose a door that does not exist. Game Over!")
      
else:
  print("You get attacked by an angry trout. Game Over")

