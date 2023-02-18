#This is my first code in Python, I have made many modifications since its conception. Please check previous versions.

#Ingredients list
ingredients = {
    "Extra Patty": 8.00,
    "American Cheese Slice": 1.00,
    "Avocado": 2.50,
    "Egg": 2.00,
    "Crisp Onion": 1.00,
    "Caramelized Onion": 1.50,
    "Raw Onion": 0.50,
    "Lettuce": 0.50,
    "Coleslaw": 1.00,
    "Pickled Cucumber": 0.50,
    "Sweet Relish": 1.00,
    "Tomato Slices": 0.70,
    "BBQ Sauce": 0.50,
    "Special Sauce": 0.50,
    "Worcester Sauce": 0.75,
    "Mayo": 0.20
}

#Beverages list
beverages = {
    "Soda": 3.00,
    "Juice": 4.00,
    "Energy Drink": 6.00,
    "Beer": 8.00,
    "Milkshake": 8.00
}

#Function to the take the customer's burger order
def take_order():
    burger = ['Bun', 'Patty']
    total = 11.0  # Start with the cost of bun and patty
    print('Every burger starts with one patty and a bun.\nYou can add anything else from this list of available ingredients: \n')
    for ingredient, price in ingredients.items():
        print(f"{ingredient}: ${price}")
    print()

    #Prompt the customer to choose the ingredients
    while True:
        ingredient = input("Please choose an ingredient and type 'done' if your burger is complete: ").lower()
        if ingredient == "done":
            break
        elif ingredient not in (i.lower() for i in ingredients):
            print("Sorry, that ingredient is not available.\n")
        else:
            for i in ingredients:
                if i.lower() == ingredient:
                    burger.append(i)
                    total += ingredients[i]
                    break
    print("Your burger has the following ingredients: ")
    print(', '.join(burger))
    return total


#Function to get the customer's beverage order
def get_beverage():
    total = 0.0
    drinks = []

    #Prompt the customer to choose a beverage
    while True:

        print("Great! These are the beverages available:\n")
        for b, price in beverages.items():
            print(f"{b}: ${price}")
        print()

        while True:
            drink = input("Please choose the ones you would like and type 'done' when you're finished choosing: ")
            if drink == "done":
                break
            elif drink not in (b.lower() for b in beverages):
                print("Sorry, this beverage is not available.\n")
            else:
                for b, price in beverages.items():
                    if b.lower() == drink:
                        drinks.append(b)
                        total += price
                        break
        print("\nOk, so the following drinks are coming up: ")
        print(', '.join(drinks))
        print()
        return total


def main():
    order_total = take_order()
    wants_beverage = input("\nWould you like a beverage with your order? (Yes/No): ").lower()
    if wants_beverage == "yes":
        beverage_total = get_beverage()
        total = order_total + beverage_total
    else:
        total = order_total
    print(f"\nYour total is ${total:.2f}. Lets proceed to the payment.")

    while True:
        payment = input("\nWould you like to pay by cash or card? (Cash/Card): ").lower()
        if payment == "cash":
            try:
                cash = float(input("How much in cash are you paying with? $"))
            except ValueError:
                print("Please enter a valid amount in dollars.")
                continue
            if cash >= total:
                print("Here's your change, ${:.2f}".format(cash - total))
                break
            else:
                print("Sorry, that's not enough to cover the total.")
        elif payment == "card":
            print("You may insert your card into the machine and enter your PIN, or tap it if you have contactless payment.\n")
            break
        else:
            print("Invalid payment method, please try again.") 

import random
table = random.randrange(1, 31) 

names = ["Natasha", "Wendy", "Yuna", "Melissandre", "June", "Celeste", "Sarah", "Maybelle", "Rose", "Mona", "Triss", "Jenn", "Yessi"]
attname = random.choice(names)

#Program starts here
name = input ("Hello there, I'm {}! What's your name? ".format(attname))
print ('\nWelcome to Burger Palace, {}!'.format (name))
print ('''Here we say "there's no burger we can't make".\n''')

main()

print (f"""Ok, your table number is {table}. 
As soon as your order is ready, we will serve it on your table.\n
Thank you for choosing Burger Palace!
We hope to see you again.""")
