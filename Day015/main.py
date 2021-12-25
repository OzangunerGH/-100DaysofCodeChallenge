from menu import drinks

machine_supplies = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def sufficient_resources(drink, stock_supplies):
    """Returns True when order can be made, False if ingredients are insufficient."""
    required_supplies = {}
    enough_supplies = True
    for keys in drink["ingredients"]:
        if keys == "water":
            required_supplies[keys] = drink["ingredients"][keys]
        elif keys == "milk":
            required_supplies[keys] = drink["ingredients"][keys]
        elif keys == "coffee":
            required_supplies[keys] = drink["ingredients"][keys]
    for ingredient in required_supplies:
        if stock_supplies[ingredient] < required_supplies[ingredient]:
            print(f"Sorry, the {required_supplies[ingredient]} in the machine is not enough.")
            enough_supplies = False
    return enough_supplies


def make_coffee(required_supplies):
    """Deduct the required ingredients from the resources."""
    for ingredient in required_supplies:
        machine_supplies[ingredient] -= required_supplies[ingredient]
    return machine_supplies


def transaction_is_successful(choice, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    print(f"Your drink costs {drink_cost}$\n")
    global profit
    pennies = float(input("Input the amount of pennies\n"))
    dimes = float(input("Input the amount of dimes\n"))
    nickels = float(input("Input the amount of nickles\n"))
    quarters = float(input("Input the amount of quarters\n"))
    total_input = (0.01 * pennies) + (0.05 * nickels) + (0.1 * dimes) + (0.25 * quarters)
    if total_input > drink_cost:
        change = round((total_input - drink_cost), 2)
        print(f"Here's your {choice} ☕️. Enjoy it!\n")
        print(f"Here's your change {change}$ back.")
        return True
    elif total_input == drink_cost:
        profit += float(drink_cost)
        print(f"Here's your {choice}. Enjoy it!\n")
        return True
    else:
        shortage = round((drink_cost - total_input), 2)
        print(f"Your drink cost is {drink_cost}. You need {shortage}$ more. Here's your refund {total_input}$")
        return False


repeat = True
while repeat:
    choice = input("What would you like to drink? espresso/latte/cappuccino?").lower()
    drink = drinks[choice]
    stock_is_enough = sufficient_resources(drink, machine_supplies)
    if choice == "off":
        repeat = False
    elif choice == "report":
        print(f"Machine's current supplies are: {machine_supplies}.")
    else:
        if stock_is_enough and transaction_is_successful(choice, drink['cost']):
            machine_supplies = make_coffee(drink['ingredients'])
            print(f"Remaining supplies in the machine: {machine_supplies}")
    print(f"Total profit is : {profit}$\n")
    another_drink = input("Would you like another drink? Type y for yes, n for no\n")
    if another_drink == "n":
        repeat = False
