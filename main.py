MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_availability(ingredients):
    """Returns True if sufficient ingredients, False if not"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
           print(f'Sorry there is not enough {item}.')
           return False
    return True


def process_coins():
    """Return total amount of money inserted"""
    total = int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.1
    total += int(input('How many nickles?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total


def is_transaction_succesful(money_received, drink_cost):
    """Return True when payment accepted, or False when money insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change.')
        global profit
        profit += drink_cost
        return True
    print('That is not enough money. Money refunded.')
    return False


def make_coffee(drink_name, drink_ingredients):
    """Deduct required ingredients from resources."""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f'Here is your {drink_name}.')


is_on = True

while is_on:
    answer = input('What would you like? (espresso/latte/cappuccino): ')

    if answer == 'off':
        is_on = False
        print('The machine is now turned off.')
    elif answer == 'report':
        print(f'''
Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${profit}
''')
    else:
        if answer in MENU:
            drink = MENU[answer]
            if check_availability(drink['ingredients']):
                payment = process_coins()
                if is_transaction_succesful(payment, drink['cost']):
                    make_coffee(answer, drink['ingredients'])
        else:
            print('This menu item does not exist.')
