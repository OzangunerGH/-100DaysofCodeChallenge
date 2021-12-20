#Defining a function to turn reeborg towards 90 degrees to east.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    # Creating a while loop to face reeborg towards north.
while is_facing_north() == False:
    turn_left()
    
   # Moving Reeborg to a position until it hits a block so at least 1 direction is blocked, to prevent it from infinitely turning right. 
while front_is_clear() == True:
    move()
#Creating a while loop to continue moving until it Reeborg reaches to destination in the priority order below:
# Move right, if not possible, move front(north),if not , turn left and repeat.
while at_goal() != True:
    if right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()
    
