import os
import random

cash = 0

def game_menu():
    
        os.system("cls")
    
        print ("****************************************************************\n**                                                            **")
        print ("**  1 = Buy                                                   **\n**                                                            **")
        print ("**  2 = Sell                                                  **\n**                                                            **")
        print ("**  3 = Inventory                                             **\n**                                                            **")
        print ("****************************************************************")
    
        menuentry = raw_input (">")
    
        try:
            menuentry = float(menuentry)
        except:
            game_menu()
        if menuentry == 1:
            buy_menu()
        elif menuentry == 2:
            sell_menu()
        elif menuentry == 3:
            inventory_menu()

def game_start():
    
    os.system("cls")
    
    print ("****************************************************************\n**                                                            **")
    print ("**                         Drug Lord                          **\n**                                                            **")
    print ("****************************************************************\n**                                                            **")

    usr_name = raw_input("What is your handle.\n>")
    
    #Menu for difficulty
    while True:
    
        os.system("cls")
    
        print ("****************************************************************\n**                                                            **")
        print ("**  1 = Easy    $100                                          **\n**                                                            **")
        print ("**  2 = Medium  $50                                           **\n**                                                            **")
        print ("**  3 = Hard    $10                                           **\n**                                                            **")
        print ("****************************************************************")
    
        menuentry = raw_input (">")
    
        try:
            menuentry = float(menuentry)
        except:
            continue
	
        if menuentry == 1:
            cash = 100
            game_menu()
        elif menuentry == 2:
            cash = 50
            game_menu()
        elif menuentry == 3:
            cash = 10
            game_menu()
        else:
            continue
            
    return usr_name
            
# FAQ main menu v 0.2
def mainmenu ():

    os.system("cls")

    print ("****************************************************************\n**                                                            **")
    print ("**                         Main Menu                          **\n**                                                            **")
    print ("****************************************************************\n**                                                            **")
    print ("**  1 = New Game                                              **\n**                                                            **")
    print ("**  2 = Resume Game                                           **\n**                                                            **")
    print ("**  3 = High Scores                                           **\n**                                                            **")
    print ("**  8 = Credits                                               **\n**                                                            **")
    print ("**  9 = exit                                                  **\n**                                                            **")
    print ("****************************************************************")
    
    menuentry = raw_input (">")
    
    try:
		menuentry = float(menuentry)
    except:
		mainmenu ()
	
    if menuentry == 1:
        game_start()
    elif menuentry == 2:
        continue_game()
    elif menuentry == 3:
        highscoor()
    elif menuentry == 9:
        os.system("cls")
        exit ()
    else:
        mainmenu ()

# FAQ Loading screen  
def loadingscreen ():
        
    os.system("cls")  
        
    print ("****************************************************************\n**                                                            **")
    print ("**   FFFFFF                  AAA                  QQQQ        **")
    print ("**   FF                     AA AA                QQ  QQ       **")
    print ("**   FFFF                  AA   AA              QQ  Q QQ      **")
    print ("**   FF                   AAAAAAAAA              QQ  QQ       **")
    print ("**   FF                  AA       AA              QQQQ Q      **\n**                                                            **")
    print ("**                       Press Enter                          **\n**                                                            **")
    print ("****************************************************************")
   
    raw_input ()
    
    mainmenu ()
    

    
loadingscreen ()