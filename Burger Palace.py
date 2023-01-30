#code to test new and add content learned in Python language as I study
#nested conditionals
#random number generator
#while loops
#Error exceptions
#Lists
#Functions

#The idea is to simulate customer service in a burger joint where you are greeted, given options and place your order, total is generated and forms of payment are offered.

import random #import random function
table = random.randrange(1, 21) #setting a range to random function which is assigned to a variable, that will display a random value within that range

names = ["Natasha", "Wanda", "Yuna", "Melissandre", "June", "Celeste", "Sarah", "Maybelle", "Rose", "Mona", "Merigold", "Jenn"] #list with names
attname = random.choice(names) #variable receiving a random choice of the content inside the variable names

#Program starts here
name = input ("Hello there, I'm {}! What's your name? ".format(attname)) #string created inside double quotation marks to be able to use single quotation marks ' (apostrophe). Printing the attentand name generated by a random choice of names from a list
print ('\nWelcome to Burger Palace, {}!'.format (name))
print ('''Here we say "there's no burger we can't make".\n''') #string created inside three single quotation marks to be able to use double quotation marks and single quotation marks (apostrophe)

#declared variables outside the functions
total = 0
bevprice = 7.5
burgerprice = 15.9

#Added functions to simplify the code and give new possibilities

#Here on this function the client chooses to order a burger or not. In case the choice is True, the program proceeds to ask what is the burger name (can be typed anything), the ammount of it (ensuring an integer is typed)
#in case the input is 0, it becomes False and loops ends and 0 value is returned, if is 1 or more, then the value is returned.
def burgerchoice ():

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
            whichburger = input ('\nWhich burger would you like to order? Create anything and tell me. ')

            while True:
                try:
                    burgers = int (input ('How many {} would you like, 1, 2, 3, 54? '.format(whichburger)))
                except ValueError:
                    print ('Please inform the ammount of burgers in numbers: ')
                    continue
                if burgers < 0:
                    print ("Sorry, I didn't understand. Could you please inform the ammount of burgers you wish to order?")
                    continue
                else:
                    break

            if burgers >= 1:
                print ('\nOk, {} {} coming up.\n'.format(burgers,whichburger))
                break
            elif burgers == 0:
                burgers = 0
                print ('Oh well, no burgers then.\n')
                break
            return burgers

        else:
            print ("""Sorry, I didn't understand, you can just say "yes" or "no". """)
            continue

#Same concept as previous function
def bevchoice ():

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

#Second part of the program, functions runs and obtains returned values 
burgerchoice()
bevchoice()

#the returned values are used here to define the value of the variable "total"
total = total + (bevprice * bevammount) + (burgers * burgerprice)

#Simple loop in case both returned values are false/0
while True:
    if total == 0:
        print ("\nWell, I hope to see you again whenever you're ready order something. Bye-bye.\n")
        quit ()
    else:
        break

#Possible second order system, still in progress (for now just reply "no")
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

#Function to give "payment" options to the client, here the total is shown (previously defined obtained with the previous functions returned values) and can be chosen to paid with cash or card
#In case it choses cash, whichever amount above the total is accepted and given a "change" back
#although if it is lower than the order total, it skips and gives the client an option pay with card and in case it refuses then the "attendant" dismisses the client.
#card payment is simpler
def payment ():

    while True:
        print ('\nAlright. The order total is ${:.2f}'.format(total))
        
        payment = input ("Would you like to pay by cash or card? ").lower()
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
        else:
            print ("You may insert your card into the machine or tap.\n")
            break

#Third part of the program, run last function
payment ()

#New variable used previous returned value (in a variable) to define it
time = 3 * burgers

#Simple conditionals to proceed with the attentand script and inform the whole order to the client and forwards it to the "kitchen" accordingly, guides the client to a randomly generated table number and says goodbye
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
Thank you for choosing Burger Palace!""".format(table))

#End