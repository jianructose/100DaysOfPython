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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

gain = 0

def reporting():
    print(f"""
    Water: {resources['water']}ml
    Milk: {resources['milk']}ml
    Coffee: {resources['coffee']}ml
    Money: ${gain}
""")


keep_order = True
while input("Do you want to order? [y] or n:  ").lower() != "n" and keep_order:

    order = (input("What would you like? (1. espresso, 2. latte, 3. cappuccino)"))
    drinks = list(MENU.keys())

    if order == "report":
        reporting()
    elif (order) == "1":
        drink = "espresso"
    elif (order) == "2":
        drink = "latte"
    else:
        drink = "cappuccino"



    # TODO: 1. print report of all coffee machine resources

    # TODO: 4. check resources sufficient?
    if order not in ['report']:
        ingre = MENU[drink]['ingredients']

    # need_water = ['water']
    # need_milk = drink['milk']
    # need_coffee = drink['coffee']

        can_make = True
        for k, v in ingre.items():
            if v > resources[k]:
                print(f"Sorry, there is no enough {k} for {drinks[int(order)-1]}. Please refill :)")
                can_make = False
                break
            else:
                can_make = True

        if can_make:
            print("Please insert coins.")
            n_quarters = int(input("How many quarters?: "))
            n_dimes = int(input("How many dimes?: "))
            n_nickles = int(input("How many nickles?: "))
            n_pennies = int(input("How many pennies?: "))

            inserted_coins = [0.01*n_pennies, 0.1*n_dimes, 0.05*n_nickles, 0.25*n_quarters]
            balance = round(sum(inserted_coins), 2)
            print(f"===========================\nYour total bill is ${MENU[drink]['cost']}\nYou have entered ${balance}.")

            change = round(balance - MENU[drink]['cost'], 2)
            if change < 0:
                print(f"Uh oh, not enough coins to buy your fav {drinks[int(order)-1]}")
            else:
                gain+=MENU[drink]['cost']
                for k, v in ingre.items():
                    resources[k] -= ingre[k]
                    # resources['milk'] -= ingre['milk']
                    # resources['coffee'] -= ingre['coffee']
                print(f"Here is ${change} in change.\nHere is your {drinks[int(order)-1]} ☕. Enjoy!\n"
                      f"===========================")
