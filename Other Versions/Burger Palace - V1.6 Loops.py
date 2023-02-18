#input é semelhante ao scanf na linguagem C
#condicionais if else em ninho
#gerador de número aleatório
#loops em while
#programa para testar armazenamento de informações adquiridas pelo prompt e diversas opções de escolha

import random #random function
table = random.randrange(1, 21) #setting a range to random function

name = input ("Hello there, what's your name? ") #string created inside double quotation marks to be able to use single quotation marks ' (apostrophe)
print ('\nWelcome to Burger Palace, {}!'.format (name))
print ('''Here we say "there's no burger we can't make".\n''') #string created inside three single quotation marks to be able to use double quotation marks and single quotation marks (apostrophe)

total = 0

while True:
    choice1 = input('Would you like to order a burger? ').lower()
    if (choice1 == 'yes') or (choice1 == 'yeah'): #operador lógico "or" (caso uma das condições for verdadeira, então será verdadeira, apenas se duas condições forem falsas, será falso.)
        whichburger = input ('Which burger would you like to order? Create anything and tell me. ')
        burgers = int (input ('How many {} would you like, 1, 2, 3, 54? '.format(whichburger))) #convertendo valor adquirido na função input em int (ou float)
        
        if burgers == 0:
            print ('Oh well, no burgers then')

        elif burgers >= 0:
            patty = input ('How would you like the patty? For example, rare, medium rare, well done... any way you want! ')
            print ('\nOk, {} {} {} coming up.\n'.format(burgers,patty,whichburger)) #imprimindo inputs coletados formatando de maneira moderna
    else:
        burgers = 0
        print ('No burger, no problem.\n')

    drink = input ("Would you like any beverages? ").lower()
    if (drink == 'yes') or (drink == 'yeah'):
        bev = input ("Which beverage? We have all you can imagine, just name it! ")    
        bevammount = int (input ("How many {} would you like, 1, 2, 3? ".format(bev)))
    else:
        bevammount = 0
        print ("Ok, no drinks.")

    bevprice = 7.5
    burgerprice = 15.9

    total = total + burgerprice * burgers + bevprice * bevammount #fazendo operações aritméticas usando informações obtidas com inputs anteriores e atribuindo o total à uma nova variável

    if total == 0:
        print ("\nWell, I hope to see you someday whever you're hungry. Bye-bye.")
        quit ()

    print ('\nAlright. The order total is ${:.2f}'.format(total))

    choice2 = input ('Would you like to order anything else? ')
    if (choice2 == 'yes') or (choice2 == 'yeah'):
        continue

    else:
        print ("That's fine.\n")
        break

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
if bevammount >= 1:
    print ("Here you go, {} {}!\n". format (bevammount,bev))
    print ("You're always welcome back here at Buger Palace! Bye!")
    quit ()
if (drink == True) and (burgers == True):
    print ("Kitchen, make {} {}, client's patty is {}!! Don't forget {} {}!!\n". format (burgers,whichburger,patty,bevammount,bev))
elif (drink == False) or (burgers == True):
    print ("""-"Kitchen, make {} {}, client's patty is {}!!"\n""". format (burgers,whichburger,patty)) #three double quotation marks """ allows double quotation marks " and single quotation marks ' be used

print ("""Ok, your table number is {}. 
As soon as your order is ready, we will serve it on your table.\n
Thank you for choosing Burger Palace!""".format(table)) #three double quotation marks """ allows the string to be printed in several lines

