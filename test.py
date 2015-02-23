print ("**   Main Menu  **")
print ("******************")
print ("** 1 Wizard     **")
print ("** 2 Report     **")
print ("** 8 Log Out    **")
print ("** 9 Quit       **")
print ("******************")
    
menuentry = raw_input (">")
try:
	menuentry = float(menuentry)
except:
	mainmenu ()
	
	
if menuentry == 1 :
    wizard ()
elif menuentry == 2 :
    report ()
elif menuentry == 8 :
    login ()
elif menuentry == 9 :
    quit ()
else :
	mainmenu ()