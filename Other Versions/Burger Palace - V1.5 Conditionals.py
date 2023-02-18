#nested conditionals
#random number generator
#programa para testar armazenamento de informações adquiridas pelo prompt e diversas opções de escolha

import random
table = random.randrange(1, 21)

name = input ("Hello there, what's your name? ") #string created inside double quotation marks to be able to use single quotation marks ' (apostrophe)
print ('\nWelcome to Burger Palace, {}!'.format (name)) #imprimindo input coletado formatando de maneira moderna
print ('''Here we say "there's no burger we can't make".\n''') #string created inside three single quotation marks to be able to use double quotation marks and single quotation marks (apostrophe)

whichburger = input ('Which burger would you like to order? Create anything and tell me. ')
burgers = int (input ('How many {} burger would you like, 1, 2, 3? '.format(whichburger))) #convertendo valor adquirido na função input em int (ou float)
patty = input ('How would you like the patty? Rare, medium rare or well done? ')
print ('\nOk, {} {} {} coming up.\n'.format(burgers,patty,whichburger)) #imprimindo inputs coletados formatando de maneira moderna

drink = input ("Would you like any beverages? ").lower()
if drink == "yes":
    bev = input ("Wich beverage to go with? We have all you can imagine, just name it! ")    
    bevammount = int (input ("How many {} would you like, 1, 2, 3? ".format(bev)))
else:
    bevammount = 0
    print ("Ok, no drinks.")

bevprice = 7.5
burgerprice = 15.9
total = burgerprice * burgers + bevprice * bevammount #fazendo operações aritméticas usando informações obtidas com imputs anteriores e atribuindo o total à uma nova variável
print ('\nAlright. The order total is ${}'.format(total)) 

payment = input ("Would you like to pay by cash or card? ").lower() #lots of nested conditionals
if payment != "card":
    cash = float (input ("How much in cash are you paying with? $"))
    if cash > total:
        print ("Here's your change, ${}.\n".format(cash-total))  
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
print ('Your order will be ready in approximately {} minutes\n'.format (time))
if drink == "yes":
    print ("Kitchen, make {} {}, client's patty is {}!!! Don't forget {} {}!!!!\n". format (burgers,whichburger,patty,bevammount,bev))
else:
    print ("Kitchen, make {} {}, client's patty is {}!!!!!!\n". format (burgers,whichburger,patty))

print ("""Ok, your table number is {}. 
As soon as your order is ready, we will serve it on your table.\n
Thank you for choosing Burger Palace!""".format(table)) #three double quotation marks """" allows the string to be printed in several lines
