#nested conditionals
#random number generator
#while loops
#code to test new and add content learned in Python language as I study

#The idea is to simulate customer service in a burger joint where you are greeted, given options and place your order

import random #random function
table = random.randrange(1, 21) #setting a range to random function

name = input ("Hello there, what's your name? ") #string created inside double quotation marks to be able to use single quotation marks ' (apostrophe)
print ('\nWelcome to Burger Palace, {}!'.format (name))
print ('''Here we say "there's no burger we can't make".\n''') #string created inside three single quotation marks to be able to use double quotation marks and single quotation marks (apostrophe)

total = 0

while True:
    choice1 = input('Would you like to order a burger? ').lower()
    if (choice1 == 'yes') or (choice1 == 'yeah') or (choice1 == 'y'): #logical operador "or" (in case one of the conditions is true, then the outcome will be True, in case one or more of the conditions is false, then the outcome will be False)

        whichburger = input ('Which burger would you like to order? Create anything and tell me. ')

        burgers = int (input ('How many {} would you like, 1, 2, 3, 54? '.format(whichburger))) #converting acquired values through input to integer

        if burgers == 0:
            print ('Oh well, no burgers then')

        elif burgers >= 1:
            patty = input ('How would you like the patty? For example, rare, medium rare, well done... any way you want! ')
            print ('\nOk, {} {} {} coming up.\n'.format(burgers,patty,whichburger))
    else:
        burgers = 0
        print ('No burger, no problem.\n')

    drink = input ("Would you like any beverages? ").lower()
    if (drink == 'yes') or (drink == 'yeah') or (drink == 'y'):
        bev = input ("Which beverage? We have all you can imagine, just name it! ")
        bevammount = int (input ("How many {} would you like, 1, 2, 3? ".format(bev)))

    else:
        bevammount = 0
        print ("Ok, no drinks.")

    bevprice = 7.5
    burgerprice = 15.9

    total = total + burgerprice * burgers + bevprice * bevammount #basic math operations based on variables values

    if total == 0:
        print ("\nWell, I hope to see you someday whever you're hungry. Bye-bye.")
        quit ()

    print ('\nAlright. The order total is ${:.2f}'.format(total))
    break

#payment choices
payment = input ("Would you like to pay by cash or card? ").lower() #lots of nested conditionals
if payment != "card":
    cash = float (input ("How much in cash are you paying with? $"))
    if cash > total:
        print ("Here's your change, ${:.2f}\n".format(cash - total))  
    if cash < total:
        print ("I'm sorry, this isn't enough to cover the total.")
        choice = input ("\nWould you like to pay by card instead? ").lower()
        if choice == "yes":
            print ("You may insert your card into the machine or tap.\n")
        else:
            print ("Ok, we hope to see you back someday.")
            quit ()
else:
    print ("You may insert your card into the machine or tap.\n")
    
time = 3 * burgers

if time >= 1:
    print ('Your order will be ready in approximately {} minutes\n'.format (time))

if (bevammount >= 1) and (burgers == 0):
    print ("Here you go, {} {}!\n". format (bevammount,bev))
    print ("You're always welcome back here at Buger Palace! Bye!")
    quit ()
    
elif (bevammount >= 1) and (burgers >= 1):
    print ("Kitchen, make {} {}, client's patty is {}!! Don't forget {} {}!!\n". format (burgers,whichburger,patty,bevammount,bev))
    
elif (bevammount == 0) and (burgers >= 1):
    print ("""-"Kitchen, make {} {}, client's patty is {}!!"\n""". format (burgers,whichburger,patty)) #three double quotation marks """ allows double quotation marks " and single quotation marks ' be used

print ("""Ok, your table number is {}. 
As soon as your order is ready, we will serve it on your table.\n
Thank you for choosing Burger Palace!""".format(table)) #three double quotation marks """ allows the string to be printed in several lines