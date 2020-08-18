from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
import sys

def hello():
    print('Hello Nattapong')

def hello2(event): # การ bind ต้องส่งพารามิเตอร์เข้าไปด้วย
    # Message Box
    # messagebox.showinfo(title='Message', message='Hello User.')
    # ลักษณะการแจ้งเตือน
    # messagebox.showwarning(title='Alert',message='Virus alert')
    # ลักษณะการถามแบบยืนยัน
    status = messagebox.askyesno(title='Question', message='Confirm') # ลักษณะการถามแบบยืนยัน
    if status>0: # ตรวจสอบค่าจาก Message Box จะเก็บค่าเป็น Int
        sys.exit()

def CloseMenu(even):
    sys.exit()

def fColor(event):
    # Color Dialog
    mycolor = colorchooser.askcolor()
    mlable = Label(text=mycolor).pack()

def fOpen(event):
    # Open file
    myfile = filedialog.askopenfile()
    FileLabel = Label(text=myfile).pack()

# Create GUI
gui = Tk()
gui.geometry("900x600+300+200")
gui.title("My First Frame.")

# Create Label
lbl1 = Label(text="Nattapong Ngamphak", bg="gray", fg="white")\
    .pack()

# Ceate Button
btn1 = Button(text="Submit", command=hello)\
    .pack()
btn2 = Button(text="Hello")
btn2.bind('<Button-1>', hello2) # Button - 1 คือการคลิก
btn2.pack()

btn3 = Button(text="Color")
btn3.bind('<Button-1>', fColor)
btn3.pack()

btn4 = Button(text="Open File :")
btn4.bind('<Button-1>', fOpen)
btn4.pack()

# Create Textbox
txt1 = Entry().pack()

# Create Menu File
menufile = Menu(gui)
FileMenu = Menu(menufile, tearoff=0)
FileMenu.add_command(label="New")
FileMenu.add_command(label="Open", command=filedialog.askopenfile) # เมื่อคลิก Open จะเป็นการเปิดไฟล์
FileMenu.add_command(label="Save")
FileMenu.add_command(label="Close", command=sys.exit) # เมื่อคลิก Close หน้าต่างจะปิด
menufile.add_cascade(label="File", menu=FileMenu)

# Create Menu Edit
EditMenu = Menu(menufile, tearoff=0)
EditMenu.add_command(label="Undo Typing")
EditMenu.add_command(label="Redo")
EditMenu.add_command(label="Cut")
EditMenu.add_command(label="Copy")
EditMenu.add_command(label="Paste")
EditMenu.add_command(label="Delete")
menufile.add_cascade(label="Edit", menu=EditMenu) # เอาตัวแปร EditMenu ใส่ในแถบ menufile

# Create Menu View
ViewMenu = Menu(menufile, tearoff=0)
ViewMenu.add_command(label="Recent File")
ViewMenu.add_command(label="Tool Windows")
ViewMenu.add_command(label="Recent File")
ViewMenu.add_command(label="Appearance")
menufile.add_cascade(label="View", menu=ViewMenu)

gui.config(menu=menufile)
#gui.config(menu=MenuEdit)

# Create Radio Button *****
rdoMale = Radiobutton(text="Male", value=1).pack()
rdoFemale = Radiobutton(text="Female", value=2).pack()

# spinbox *******
spin1 = Spinbox(from_=0,to=10).pack()
# ใน spinbox from_=0 คือค่าจะเริ่งต้นคือ 0 to=10 คือค่าเท่ากับ 10

# listbox ********
listbox1 = Listbox()
listbox1.insert(1,"Python")
listbox1.insert(2,"Nattapong")
listbox1.insert(3,"Niracha")
listbox1.pack()

# slidebar
sli1 = Scale(orient=HORIZONTAL, width=20, length=300, from_=0, to=100, tickinterval=10)
# default จะเป็นแนวตั้งแต่กำหนดได้โดยใส่ orientation
sli1.pack()


gui.mainloop()











