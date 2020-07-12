from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys


print(sys.version)

# put function here



gui = Tk()
gui.geometry("500x500+300+200")
gui.title('Mainmenu')
gui.resizable(0, 0) # Don't able to drag resize windows

btn_user = ttk.Button(text='Eletric Price Page.').place(width=300, height=50, x=100, y=20)
btn_product = ttk.Button(text='Product').place(width=300, height=50, x=100, y=80)
#btn_test = ttk.Button(text='Test Order From').place(width=250, height=50, x=140, y=140)
#
gui.mainloop()
