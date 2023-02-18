menu = {"Extra Patty": 8.00,
        "American Cheese Slice": 1.00,
        "Avocado": 2.50,
        "Egg": 2.00,
        "Crisp Onion": 1.00,
        "Caramelized Onion": 1.50,
        "Raw Onion": 0.50,
        "Lettuce": 0.50,
        "Coleslaw": 1.00,
        "Picled Cucumber": 0.50,
        "Sweet Relish": 1.00,                        
        "Tomato Slices": 0.70,                        
        "BBQ Sauce": 0.50,
        "Special Sauce": 0.50,
        "Mayo": 0.20}

beverages = {"Soda": 3.00,
        "Juice": 4.00,
        "Energy Drink": 6.00,
        "Beer": 8.00,
        "Milkshake": 8.00}

import random
table = random.randrange(1, 21) 

names = ["Natasha", "Wanda", "Yuna", "Melissandre", "June", "Celeste", "Sarah", "Maybelle", "Rose", "Mona", "Merigold", "Jenn"]
attname = random.choice(names)

#Program starts here
name = input ("Hello there, I'm {}! What's your name? ".format(attname))
print ('\nWelcome to Burger Palace, {}!'.format (name))
print ('''Here we say "there's no burger we can't make".\n''')

def burger_order ():

    while True:
        global meal
        meal = input('Would you like to order a burger? ').lower()
        
        global burgers
        if (meal == 'no') or (meal == 'nah') or (meal == 'n') or (meal == 'nope'):
            burgers = 0
            print ('No burger, no problem.\n')
            break

        elif (meal == 'yes') or (meal == 'yeah') or (meal == 'y'):
            global whichburger
            print ('\nGreat! Every burger starts with one patty and a bun.\nYou can add anything else from this is a list of available ingredients: \n')

        for ingredient, price in menu.items():
            print(f"{ingredient} - ${price:.2f}")

            while True:
                whichburger = input ('\nWhat would you like on your burger? (Please separate ingredients with commas.)\n')
                
                return whichburger




        else:
            print ("""Sorry, I didn't understand, you can just say "yes" or "no". """)
            continue

burger_order ()
print (whichburger)