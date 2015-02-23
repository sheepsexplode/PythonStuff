# Bill Calculator V 0.1

import os
import random

def wizard ():
    
    print ("Enter day of the month")
    dayofthemo = raw_input (">")
    dayofthemo = float(dayofthemo)
    print ("Enter number of pay(S) remaining")
    paysleft = raw_input (">")
    paysleft = float(paysleft)
    print ("Remaining Funds")
    cashleft = raw_input ("> $")
    cashleft = float(cashleft)
    print ("******************")
    mainmenu ()

def report ():
    
    print ("Under construction")
    
    totalcash = paysleft + cashleft
   
    print totalcash

    exit ()
    
# FAQ main menu v 0.1
def mainmenu ():

    os.system("cls")

    print ("****************************************************************") 
    print ("**                                                            **")
    print ("**                         Main Menu                          **")
    print ("**                                                            **")
    print ("****************************************************************")
    print ("**                                                            **")
    print ("**  1 = Games                                                 **")
    print ("**                                                            **")
    print ("**  2 = Wizard                                                **")
    print ("**                                                            **")
    print ("**  3 = Report                                                **")
    print ("**                                                            **")
    print ("**  8 = Log Out                                               **")
    print ("**                                                            **")
    print ("**  9 = exit                                                  **")
    print ("**                                                            **")
    print ("****************************************************************")
    
    menuentry = raw_input (">")
    try:
		menuentry = float(menuentry)
    except:
		mainmenu ()
	
    if menuentry == 1:
        gamemenu()
    elif menuentry == 2:
        report ()
    elif menuentry == 8:
        login ()
    elif menuentry == 9:
        os.system("cls")
        exit ()
    else:
        mainmenu ()

# List of games        
def gamemenu ():

    os.system("cls")

    print ("****************************************************************") 
    print ("**                                                            **")
    print ("**                         Game Menu                          **")
    print ("**                                                            **")
    print ("****************************************************************")
    print ("**                                                            **")
    print ("**  1 = Guess my number                                       **")
    print ("**                                                            **")
    print ("**  2 = Craps                                                 **")
    print ("**                                                            **")
    print ("**  3 =                                                       **")
    print ("**                                                            **")
    print ("**  8 =                                                       **")
    print ("**                                                            **")
    print ("**  9 = Main Menu                                             **")
    print ("**                                                            **")
    print ("****************************************************************")
    
    menuentry = raw_input (">")
    try:
		menuentry = float(menuentry)
    except:
		gamemenu()
	
    if menuentry == 1:
        guessmynumb ()
    elif menuentry == 2:
        craps()
    elif menuentry == 9:
        mainmenu()
    else:
        gamemenu()

# Super crappy login lol
def login ():

    print "******************"
    user = raw_input ("User Name:")
    cuser = ("FAQ")
    if user != cuser:
        print ("Incorrect User Name")
        login()
    
    paswrd = raw_input ("Password:")
    cpass = ("sch00Ner")
    if paswrd != cpass:
        print ("Incorrect Password")
        login()
    
    print mainmenu ()

# FAQ Loading screen  
def loadingscreen ():
        
    os.system("cls")  
        
    print ("****************************************************************")
    print ("**                                                            **")
    print ("**   FFFFFF                  AAA                  QQQQ        **")
    print ("**   FF                     AA AA                QQ  QQ       **")
    print ("**   FFFF                  AA   AA              QQ  Q QQ      **")
    print ("**   FF                   AAAAAAAAA              QQ  QQ       **")
    print ("**   FF                  AA       AA              QQQQ Q      **")
    print ("**                                                            **")
    print ("**                       Press Enter                          **")
    print ("**                                                            **")
    print ("****************************************************************")
   
    raw_input ()
    
    mainmenu ()

# Game of Craps
def craps ():

    os.system("cls")
    
    print ("****************************************************************") 
    print ("**                                                            **")
    print ("**                           Craps                            **")
    print ("**                                                            **")
    print ("**                     Select difficulty                      **")
    print ("**                                                            **")
    print ("****************************************************************")
    print ("**                                                            **")
    print ("**  1 = Easy   $100                                           **")
    print ("**                                                            **")
    print ("**  2 = Medium  $50                                           **")
    print ("**                                                            **")
    print ("**  3 = Hard    $10                                           **")
    print ("**                                                            **")
    print ("**  9 = exit game                                             **")
    print ("**                                                            **")
    print ("****************************************************************")
        
    menuentry = raw_input (">")
    
    try:
		menuentry = float(menuentry)
    except:
		craps()
	
    if menuentry == 1:
        wallet = 100
    elif menuentry == 2:
        wallet = 50
    elif menuentry == 3:
        wallet = 10
    elif menuentry == 9:
        mainmenu()
    else:
        craps()
    
    dice1 = 1
    dice2 = 1 
    
    status = ""
    
    lastroll = 0
    
    cattempts = 1

    while wallet > 0:
    
        os.system("cls")
    
        dieprint1 = str(dice1)
        dieprint2 = str(dice2)
        walletprint = str(wallet)
        
        print ("****************************************************************") 
        print ("**                                                            **")
        print ("**                           Craps                            **")
        print ("**                                                            **")
        print ("**                     Select difficulty                      **")
        print ("**                                                            **")
        print ("****************************************************************")
        print ("")
        print ("    Dice 1")
        print ("    " + dieprint1 + "                            " + status + "\n")
        print ("    Dice 2")
        print ("    " + dieprint2)
        print ("")
        print ("    Current Cash $" + walletprint)
        print ("")
        print ("****************************************************************")
        print ("")
        print ("    What would you like to do?")
        print ("")
        print ("    Enter [R] to roll, [C] to cash out or [Q] to exit.")
        print ("")
        print ("****************************************************************")
        
        while 1 == 1:
        
            menuentry = raw_input (">")
        
            if menuentry == "r":
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                break
            elif menuentry == "c":
                wallet = 50
                break
            elif menuentry == "q":
                mainmenu ()
                
            print ("Enter good input or [Q] to exit")
        
        betcheck = 1
        
        while betcheck > 0 and cattempts == 1:
            
            bet = raw_input ("Amount to bet > $")
            
            betcheck = 0
            
            try:
                bet = float(bet)
            except:
                print ("You can't bet letters. You have $" + walletprint + " to bet.")
                betcheck = 1
                
            if bet > wallet and betcheck == 0:
                print ("Bet to high. You have $" + walletprint + " to bet.")
                betcheck = 1
            elif betcheck == 0:
                break            
    
        if dice1 + dice2 == 7 or dice1 + dice2 == 11 and cattempts == 1:
            status = "Win"
            cattempts = 1
            wallet = wallet + bet
        elif dice1 + dice2 == 2 or dice1 + dice2 == 3 or dice1 + dice2 == 12 and cattempts == 1:
            status = "Lose"
            cattempts = 1
            wallet = wallet - bet
        elif lastroll == dice1 + dice2:
            status = "Win"
            cattempts = 1
            wallet = wallet + bet
        elif cattempts > 1:
            status = "Lose"
            cattempts = 1
            wallet = wallet - bet
        else:
            status = str(dice1 + dice2)
            cattempts = cattempts + 1
            lastroll = dice1 + dice2
    
    print ("You have no cash left. Press enter to continue")
    
    raw_input()
    
    mainmenu()

# Guess my number game
def guessmynumb ():

    os.system("cls")
    
    rndnum = random.randint(1, 100)
    
    rndnumstrprttemp = str(rndnum)

# Shows the random number for testing    
#    print rndnumstrprttemp
    
    print ("Guess a number between 1 and 100. You have 10 attempts.")
    
    guesses = 0
        
    while guesses < 10:
        
        guesses = guesses + 1
        
        guessesstr = str(guesses)
        
        print ("Enter guess number " + guessesstr)
        numguess = raw_input(">")
        lastguess = numguess
        
# Validate number value and within parameters  

        inputcheck = 1
 
        while inputcheck > 0:
            
            try:
                numguess = float(numguess)
                inputcheck = 0
            except:
                print ("Please enter a number between 1 and 100")
                inputcheck = 1
                
            if numguess > 100 and inputcheck == 0:
                print ("Please enter a number under 100")
                inputcheck = 1
            elif numguess < 100 and inputcheck == 0:
                break            
    
            numguess = raw_input(">")
    
        os.system("cls")
        
        if numguess < rndnum:
            print ("Your guess is to low")
        elif numguess > rndnum:
            print ("Your guess is to high")    
        elif numguess == rndnum:
            break
        
    if numguess == rndnum:
        guesses = str(guesses)
        numguessstr = str(numguess)
        print ("You WIN! It took you " + guesses + " tries to get the number " + numguessstr)
    elif numguess != rndnum:
        rndnumstr = str(rndnum)
        print ("No Luck. The number I was thinking of was " + rndnumstr + ". Try again with a new number") 
    
    raw_input()
    
    mainmenu()
    
# Disable login for testing    
# print login ()

print loadingscreen()