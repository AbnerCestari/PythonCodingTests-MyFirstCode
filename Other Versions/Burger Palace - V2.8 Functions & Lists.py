#condicionais if else em ninho
#gerador de número aleatório
#loops em while
#exceções de erros
#Funções
#Dicionários/ Listas

cart = []
total = 0
bevprice = 7.5
burgerprice = 15.9

menu = {"Pizza": 12.00,
        "NACHOS": 13.50,
        "PIPOCA": 25.00,
        "FRITAS": 16.00,
        "HOTDOG": 14.00,
        "CHURROS": 11.00,
        "REFRI": 12.00,
        "SUCO": 10.00}

import random #import random function
table = random.randrange(1, 21) #setting a range to random function which is assigned to a variable, that will display a random value within that range

names = ["Natasha", "Wanda", "Yuna", "Melissandre", "June", "Celeste", "Sarah", "Maybelle", "Rose", "Mona", "Merigold", "Jenn"] #list with names
attname = random.choice(names) #variable receiving a random choice of the content inside the variable names

name = input ("Hello there, I'm {}! What's your name? ".format(attname)) #string created inside double quotation marks to be able to use single quotation marks ' (apostrophe). Printing the attentand name generated by a random choice of names from a list
print ('\nWelcome to Burger Palace, {}!'.format (name))
print ('''Here we say "there's no burger we can't make".\n''') #string created inside three single quotation marks to be able to use double quotation marks and single quotation marks (apostrophe)


def burgerchoice (): #a complicated function full of loops within loops and nested conditionals with exceptions

    while True:
        global meal
        meal = input('Would you like to order a burger? ').lower()
        
        global burgers
        if (meal == 'no') or (meal == 'nah') or (meal == 'n') or (meal == 'nope'):
            burgers = 0
            print ('No burger, no problem.\n')
            break

        elif (meal == 'yes') or (meal == 'yeah') or (meal == 'y'): #operador lógico "or" (caso uma das condições for verdadeira, então será verdadeira, apenas se duas condições forem falsas, será falso.)
            global whichburger
            whichburger = input ('\nWhich burger would you like to order? Create anything and tell me. ')

            while True:
                try:
                    burgers = int (input ('How many {} would you like, 1, 2, 3, 54? '.format(whichburger))) #convertendo valor adquirido na função input em int (ou float)
                except ValueError:
                    print ('Please inform the ammount of burgers in numbers: ')
                    continue
                if burgers < 0:
                    print ("Sorry, I didn't understand. Could you please inform the ammount of burgers you wish to order?")
                    continue
                else:
                    break

            if burgers >= 1:
                print ('\nOk, {} {} coming up.\n'.format(burgers,whichburger)) #imprimindo inputs coletados formatando de maneira moderna
                break
            elif burgers == 0:
                burgers = 0
                print ('Oh well, no burgers then.\n')
                break
            return burgers

        else:
            print ("""Sorry, I didn't understand, you can just say "yes" or "no". """) #triple """ quotation marks allows a string to have ' and " inside
            continue

def bevchoice (): #another complicated function

    while True:
        global drink
        drink = input ("Would you like any beverages? ").lower()

        global bevammount
        if (drink == 'no') or (drink == 'nah') or (drink == 'n') or (drink == 'nope'):
            bevammount = 0
            print ('Sure thing...')
            break
        
        elif (drink == 'yes') or (drink == 'yeah') or (drink == 'y'):
            global bev
            bev = input ("Which beverage? We have all you can imagine, just name it! ")

            while True:
                try:
                    bevammount = int (input ("How many {} would you like, 1, 2, 3? ".format(bev)))
                except ValueError:
                    print ('Please inform the ammount of beverages in numbers: ')
                    continue
                if bevammount < 0:
                    print ("Sorry, I didn't understand. Could you please inform the ammount of drinks you wish to order?")
                    continue
                if bevammount == 0:
                    bevammount = 0
                    print ('Okay, no drinks then...')
                    break
                else:
                    break
            if bevammount >= 1:
                print ('\nGot it, {} {} coming up!'.format(bevammount,bev))
                break
            return bevammount
        else:
            print ("""Sorry, I didn't understand, you can just say "yes" or "no". """)
            continue

burgerchoice()
bevchoice()

total = total + (bevprice * bevammount) + (burgers * burgerprice)

while True: #simple loop
    if total == 0:
        print ("\nWell, I hope to see you again whenever you're ready order something. Bye-bye.\n")
        quit ()
    else:
        break

#possible second order system, in progress

while True:
    order2 = input ('Would you like anything else? ')
    if (order2 == 'yes') or (order2 == 'yeah') or (order2 == 'y'):
        print ('Great!!\n')
        burgerchoice()
        bevchoice()
        break
    elif (order2 == 'no') or (order2 == 'nah') or (order2 == 'n') or (order2 == 'nope'):
        print ('Ok, no problem.')
        break
    else:
        print ("""Sorry, I didn't understand, you can just say "yes" or "no". """)
        continue

print ('\nAlright. The order total is ${:.2f}'.format(total))

def payment ():

    while True:

        payment = input ("Would you like to pay by cash or card? ").lower() #lots of nested conditionals
        if payment == "cash":

            try:
                cash = int (input ("How much in cash are you paying with? $"))
            except ValueError:
                print ('Please type a number: ')
                continue
            if cash > total:
                print ("Here's your change, ${:.2f}\n".format(cash - total))
                break
            if cash < total:
                print ("I'm sorry, this isn't enough to cover the total.")
                choice = input ("\nWould you like to pay by card instead? ").lower()
                if (choice == 'yes') or (choice == 'y') or (choice == 'yeah'):
                    print ("You may insert your card into the machine or tap.\n")
                    break
                else:
                    print ("Ok, we hope to see you back someday.")
                    quit ()
        elif (payment != 'cash') and (payment != 'card'):
            print ("Sorry, I did't understand what you said\n")
            continue

        elif payment == 'card':
            print ("You may insert your card into the machine or tap.\n")
            break

payment ()

time = 3 * burgers
 
if time >= 1:
    print ('Your order will be ready in approximately {} minutes.\n'.format (time))

if (bevammount >= 1) and (burgers == 0):
    print ("Here you go, {} {}!\n". format (bevammount,bev))
    print ("You're always welcome back here at Buger Palace! Bye!")
    quit ()

elif (bevammount >= 1) and (burgers >= 1): 
    print ("-Kitchen, make {} {}!! Don't forget {} {}!!\n". format (burgers,whichburger,bevammount,bev))
    
elif (bevammount == 0) and (burgers >= 1):
    print ('-Kitchen, make {} {}!!\n'. format (burgers,whichburger))

print ("""Ok, your table number is {}. 
As soon as your order is ready, we will serve it on your table.\n
Thank you for choosing Burger Palace!""".format(table)) #three double quotation marks """ allows the string to be printed in several lines