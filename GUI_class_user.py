from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
# test create Form width OOP
class product:
    def __init__(self, gui):
        self.win = gui
        self.win.title('Register New Product')
        self.win.geometry("360x500+300+200")
        self.win.resizable(0, 0) # Don't able to drag resize windows
        # connect database
        self.con = sqlite3.connect('Database/DB_Test.db')
        self.con.cursor()
        # Create Frame
        frame = ttk.Labelframe(self.win, text='Add new product.', width=340, height=170)
        frame.place(x=10, y=10)
        # create Label
        self.lbl_id = ttk.Label(frame, text='Product ID :').place(x=10, y=10)
        self.lbl_product =ttk.Label(frame, text='Product Name :').place(x=10, y=40)
        self.lbl_price = ttk.Label(frame, text='Product Price :').place(x=10, y=70)
        # create Textbox and variable
        self.id = StringVar()
        self.product = StringVar()
        self.price = StringVar()
        self.txt_id = ttk.Entry(frame, textvariable=self.id, width=10).place(x=90, y=10)
        self.txt_product = ttk.Entry(frame, textvariable=self.product).place(x=120, y=40)
        self.txt_price = ttk.Entry(frame, textvariable=self.product).place(x=120, y=70)
        # create button
        self.btn_save = ttk.Button(frame, text='save').place(x=120, y=100)

        # create frame for show treeview
        frame2 = ttk.Labelframe(self.win, text='Product data.', width=340, height=240)
        frame2.place(x=10, y=200)
        self.tree = ttk.Treeview()
        self.tree['show'] = 'headings'
        self.tree['columns'] = ('ID', 'Product', 'Price')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Product', text='Product')
        self.tree.heading('Price', text='Price')
        self.tree.column('ID', width=50)
        self.tree.column('Product', width=160)
        self.tree.column('Price', width=100)
        self.tree.place(x=20, y=230)



if __name__ == '__main__':
    gui = Tk()
    application = product(gui)
    gui.mainloop()