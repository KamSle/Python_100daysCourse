# 100 days with Python
# Coffee Machine Game
# DAY 15

menu = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_left(new_resources):
    water = new_resources["water"]
    milk = new_resources["milk"]
    coffee = new_resources["coffee"]
    print(f"water: {water}\nmilk: {milk}\ncoffee: {coffee}")


def ingredients_counter(type_of_drink):
    w = resources["water"] - menu[type_of_drink]["ingredients"]["water"]
    m = resources["milk"] - menu[type_of_drink]["ingredients"]["milk"]
    c = resources["coffee"] - menu[type_of_drink]["ingredients"]["coffee"]
    # resources["cost"] = menu[type_of_drink]["ingredients"]["coffee"]
    resources["water"] = w
    resources["milk"] = m
    resources["coffee"] = c
    return resources


def ingredients_checker(type_of_drink):
    for type_of_ingredient in ("water", "milk", "coffee"):
        if resources["water"] < 50:
            return 2
        elif resources[type_of_ingredient] < menu[type_of_drink]["ingredients"][type_of_ingredient]:
            print(f"Sorry there is not enough {type_of_ingredient}.")
            return 0
        else:
            return 1


def counting_money():
    print("Please insert coins.")
    quarter = int(input("How many quarters? "))
    dime = int(input("How many dimes? "))
    nickle = int(input("How many nickles? "))
    penny = int(input("How many pennies? "))
    pay = (0.25 * quarter) + (0.1 * dime) + (0.05 * nickle) + (0.01 * penny)
    if pay > cost:
        rest = pay - cost
        print(f"Here is your {rest} in change!\nHere is your coffee {drink} Enjoy!")
    elif pay < cost:
        print("Sorry that's not enough money! Money refunded")
    else:
        print(f"Here is your coffee {drink} Enjoy!")
    return pay


#
# def coffee_maker(drink_type):
#     if ingredients_checker(drink_type) == 1:
#         cost = menu[drink_type]["cost"]
#         payment = counting_money()
#         resources = ingredients_counter(drink_type)
#         return True
#     else:
#         return False

print("Hi, I am your coffee machine. You can try to buy some coffee, make a 'report' or turn me 'off'.")
game_on = True
while game_on:
    drink = input("What would you like to drink? Choose between espresso / latte / cappuccino: ").lower()
    if drink == "off":
        break
    elif drink == "report":
        resources_left(resources)
    elif drink == "espresso":
        if ingredients_checker("espresso") == 1:
            cost = menu["espresso"]["cost"]
            cost = float(cost)
            menu["espresso"]["ingredients"]["milk"] = 0
            payment = counting_money()
            resources = ingredients_counter("espresso")
        elif ingredients_checker("espresso") == 2:
            print("There is nothing you can buy anymore, sorry :(")
            break
    elif drink == "latte":
        if ingredients_checker("latte") == 1:
            cost = menu["latte"]["cost"]
            cost = float(cost)
            payment = counting_money()
            resources = ingredients_counter("latte")
        elif ingredients_checker("latte") == 2:
            print("There is nothing you can buy anymore, sorry :(")
            break
    elif drink == "cappuccino":
        if ingredients_checker("cappuccino") == 1:
            cost = menu["cappuccino"]["cost"]
            cost = float(cost)
            payment = counting_money()
            resources = ingredients_counter("cappuccino")
        elif ingredients_checker("cappuccino") == 2:
            print("There is nothing you can buy anymore, sorry :(")
            break
    else:
        print("Wrong choice!")