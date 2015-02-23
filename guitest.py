
# GUI Testing

# Import all Tkinter GUI tool
from Tkinter import *
# Makes it look better
from ttk import *

# Defines the window as root
root = Tk()

# 
root.title("FAQ Testing Window")
root.geometry("500x500")

app = Frame(root)
app.grid()

msg = Label(app, text="****************************************************************\n**                                                            **\n**   FFFFFF                  AAA                  QQQQ        **\n**   FF                     AA AA                QQ  QQ       **\n**   FFFF                  AA   AA              QQ  Q QQ      **\n**   FF                   AAAAAAAAA              QQ  QQ       **\n**   FF                  AA       AA              QQQQ Q      **\n**                                                            **\n**                       Press Enter                          **\n**                                                            **\n****************************************************************") #, font="courier").pack()
        
msg.grid()

button1 = Button(app, text = "Quit")
button1.grid()


# Starts loop to keep window open
root.mainloop()