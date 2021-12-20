#Getting inputs from user such as bill amount, tip percentage, and number of people to divide

bill = input("What was the total bill?")
tip_percentage = input("How much tip would you like to give? 10, 12 or 15?")
number_of_people = input("How many people to split the bill?")

#Converting data types to suitable types for calculation

bill = float(bill)
tip_percentage = int(tip_percentage)
number_of_people = int(number_of_people)

#Necessary math operations to calculate the amount per person

tip = bill * (tip_percentage)/100
pay_per_person = (bill + tip) /number_of_people
pay_per_person = round(pay_per_person, 2)

#Printing the output
print(f"Each person should pay: {pay_per_person}")

