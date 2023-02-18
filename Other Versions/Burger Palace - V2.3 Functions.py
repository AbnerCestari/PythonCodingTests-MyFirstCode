#condicionais if else em ninho
#gerador de número aleatório
#loops em while
#exceções de erros
#Funções
#dicionários

import random #import random function
table = random.randrange(1, 21) #setting a range to random function which is assigned to a variable, that will display a random value within that range

names = ["Natasha", "Anabelle", "Wanda", "Yuna", "Melisandre", "June", "Cersei", "Sarah", "Maybelle", "Rose", "Mona"] #list with names
attname = random.choice(names) #variable receiving a random choice of the content inside the variable names

name = input ("Hello there, I'm {}! What's your name? ".format(attname)) #string created inside double quotation marks to be able to use single quotation marks ' (apostrophe). Printing the attentand name generated by a random choice of names from a list
print ('\nWelcome to Burger Palace, {}!'.format (name))
print ('''Here we say "there's no burger we can't make".\n''') #string created inside three single quotation marks to be able to use double quotation marks and single quotation marks (apostrophe)

total = 0

def burgerchoice ():

    while True:
        global choice1
        choice1 = input('Would you like to order a burger? ').lower()
        if (choice1 == 'yes') or (choice1 == 'yeah') or (choice1 == 'y'): #operador lógico "or" (caso uma das condições for verdadeira, então será verdadeira, apenas se duas condições forem falsas, será falso.)
            whichburger = input ('\nWhich burger would you like to order? Create anything and tell me. ')

            while True:
                try:
                    global burgers
                    burgers = int (input ('How many {} would you like, 1, 2, 3, 54? '.format(whichburger))) #convertendo valor adquirido na função input em int (ou float)
                except ValueError:
                    print ('Please type a number: ')
                    continue
                else:
                    break

            if burgers == 0:
                burgers = 0
                print ('Oh well, no burgers then')
                break
            elif burgers >= 1:
                print ('\nOk, {} {} coming up.\n'.format(burgers,whichburger)) #imprimindo inputs coletados formatando de maneira moderna
                break

        elif choice1 == 'no':
            print ('No burger, no problem.\n')
            break
        else:
            print ("Sorry, I didn't understand, would like a burgere, yes or no? ")
            continue

def bevchoice ():

    while True:
        global drink
        drink = input ("Would you like any beverages? ").lower()
        if (drink == 'yes') or (drink == 'yeah') or (drink == 'y'):
            bev = input ("Which beverage? We have all you can imagine, just name it! ")

            while True:
                try:
                    global bevammount
                    bevammount = int (input ("How many {} would you like, 1, 2, 3? ".format(bev)))
                except ValueError:
                    print ('Please type a number: ')
                    continue
                else:
                    break

            if bevammount == 0:
                bevammount = 0
                print ('Oh well, no drinks then')
                break
            elif bevammount >= 1:
                print ('Got it, {} {} coming up!'.format(bevammount,bev))
                break
        elif drink == 'no':
            print ('Huh, not thirsty...')
            bevammount = 0
            break
        else:
            print ("Sorry, I didn't understand, would like a beverage, yes or no? ")
            continue

bevprice = 7.5
burgerprice = 15.9

burgerchoice()
bevchoice()

total = total + (burgerprice * burgers) + (bevprice * bevammount) #fazendo operações aritméticas usando informações obtidas com dentro de funções anteriores com variáveis globais e atribuindo o total à uma nova variável

while True:
    if total == 0:
        print ("\nWell then, I hope to see you someday whever you're hungry. Bye-bye.")
        quit ()
    else:
        break



def payment ():

    print ('\nAlright. The order total is ${:.2f}'.format(total))
    
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

payment ()

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
