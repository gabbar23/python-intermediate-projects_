import os

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

# def report(water,milk,coffee,cash):


profit=0
#coin function

def coins():
    quarters=int(input("Enter the Number of Quaters"))
    dimes=int(input("Enter the number of Dimes"))
    nickles=int(input("Enter the Number of Nickles"))
    pennies=int(input("Enter the Number of pennies"))
    total=(quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    return (round(total,2))



def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry! We are out of {item}")
            return False
        return True



def is_transaction_done(coins,coffe_cost):
    if coffe_cost>coins:
        print("Sorry thats not Enough money! Money refunded!")
        return False
    elif coins>=coffe_cost:
        if coins>coffe_cost:
            refund=coins-coffe_cost
            refund=round(refund,2)
            print(f"Here is Your {refund} $ Change !")
            global profit
            profit+= coffe_cost
            return True
        return True



def prepare_coffee(coffe_name,coffe_ingredients):
    for item in coffe_ingredients:
        resources[item]-=coffe_ingredients[item]
    print(f"Here is your {coffe_name}! ")
#






not_end=True
while not_end:
    coffe=input("What would you like? espresso/latte/cappuccino ")
    if coffe=='turn off':
        not_end = False
    elif coffe=='report':
        for item in resources:
            print(f"{item}:{resources[item]}")
    else:
        drink=MENU[coffe]
        if is_resources_sufficient(drink["ingredients"]):
            coin=coins()
            if is_transaction_done(coin,MENU[coffe]['cost']):
                prepare_coffee(coffe,drink["ingredients"])




