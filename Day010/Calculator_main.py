from art import logo

## Defining operation functions

def add(n1,n2):
  return n1+ n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1 /n2
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
## Defining the calculator function
def calculator():

  ## Getting the first input number, setting repeat variable of the function to True, and printing operations symbols(+,-,*,/) for better user experience.
  number1 = float(input("Please enter the first number\n"))
  should_continue = True
  for symbol in operations:
    print(symbol)
   ## Setting up the recursive loop as long as user wants to continue. If the user says yes to operate with the previous result, number1 becomes equal to the last operation's result.
  while should_continue:
    operation_symbol = str(input("Please enter one of the operations above to calculate.\n"))
    number2 = float(input("Please enter the next number\n"))
    result= operations[operation_symbol](number1,number2)
    print(f"{number1} {operation_symbol} {number2} = {result}")
    user_repeat = input(f"If you wanna continue to operate with {result}, type yes. To restart, type no. To exit, type exit.\n").lower()
    if user_repeat == "yes":
      number1 = result
    elif user_repeat == "no":
      should_continue = False
      calculator()
    else:
      break
      print("Goodbye.") 
print(logo)
calculator()
  

