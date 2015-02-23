guesses = 0
    
rndnum = random.randint(1, 100)
    
print ("Guess a number between 1 and 100")
    
def guesswhile ()
    while guesses < 10:
       print ("Enter first guess")
       numguess = raw_input(">")
    
        try:
            numguess = float(numguess)
        except:
            print ("Please enter a number between 1 and 100")
            guesswhile()
    
    guesses = guesses + 1
        
    if numguess < rndnum:
        print ("Your guess is to low")
            
    if numguess > rndnum:
        print ("Your guess is to high")
            
    if numguess == rndnum:
        break
    
guesswhile ()
    
if numguess == rndnum:
    guesses = str(guesses)
    numguessstr = str(numguess)
    print ("You WIN! It took " + guesses + " to get the number " + numguessstr)
        
if number != rndnum:
    numguessstr = str(numguess)
    print ("No Luck. The number I was thinking of was " + numguessstr + ". Try again with a new number") 
  
