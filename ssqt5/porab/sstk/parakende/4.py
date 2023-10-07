from tkinter import *
# ~ import tkMessageBox
# ~ import Tkinter

top = Tk()

# ~ def helloCallBack():
   # ~ tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Button(top, text ="Hello")

# ~ B.pack()
B.place(bordermode=OUTSIDE, relx= 0.3, rely= 0.20, relheight=0.5, relwidth=0.5)
top.mainloop()
