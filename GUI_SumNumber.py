from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
from tkinter import messagebox
import sys

# function
def Fun_Add():
    global strAdd
    global strAdd2
    global strSum

    readAdd = float(strAdd.get())
    readAdd2 = float(strAdd2.get())

    Sum = readAdd+readAdd2
    # messagebox.showinfo(title='Sum Number', message=Sum)
    strSum.set(Sum) # นำ Sum ไปแสดงใน TextboxSum

def Fun_Minus():
    readAdd = float(strAdd.get())
    readAdd2 = float(strAdd2.get())

    if readAdd2 > readAdd:
        messagebox.showwarning(title='Alert', message='Number 2 is more Number 1')
        return
    else:
         Sum = readAdd - readAdd2
         # messagebox.showinfo(title='Sum Number', message=Sum)
         strSum.set(Sum)  # นำ Sum ไปแสดงใน TextboxSum


def Fun_Mul():
    readAdd = float(strAdd.get())
    readAdd2 = float(strAdd2.get())
    Sum = readAdd*readAdd2
    # messagebox.showinfo(title='Sum Number', message=Sum)
    strSum.set(Sum) # นำ Sum ไปแสดงใน TextboxSum

def Fun_Div():
    readAdd = float(strAdd.get())
    readAdd2 = float(strAdd2.get())
    if readAdd2 <= 0:
        messagebox.showwarning(title='Alert', message='Number 2 is zero is not impossible')
        return
    else:
         Sum = readAdd / readAdd2
         # messagebox.showinfo(title='Sum Number', message=Sum)
         strSum.set(Sum)  # นำ Sum ไปแสดงใน TextboxSum


def clear_textbox():
    strAdd.set('')
    strAdd2.set('')
    strSum.set('')

# Create gui
gui = Tk()
gui.geometry("360x250+300+200")
gui.title('Sum Number ')

# Create Label
lblSum = ttk.Label(gui, text='Sun of three number.').pack()
lblNum1 = Label(gui, text='Number 1 :').place(x=20, y=30)
lblNum2 = Label(gui, text='Number 2 :').place(x=20, y=60)
lblSumNum = Label(gui, text="Sum Number :").place(x=20, y=90)

# Create Textbox and stringvar เพื่ออ่านค่า
strAdd = StringVar()
strAdd2 = StringVar()
strSum = StringVar()
strDiv = StringVar()
txtNumber1 = ttk.Entry(textvariable=strAdd).place(x=130, y=30)
txtNumber2 = ttk.Entry(textvariable=strAdd2).place(x=130, y=60)
txtSumber = ttk.Entry(textvariable=strSum, state=DISABLED).place(x=130, y=90)

# Create Button
btnAdd = ttk.Button(gui, text='+', command=Fun_Add).place(x=130, y=130)
btnMinus = ttk.Button(gui, text='-', command=Fun_Minus).place(x=130, y=160)
btnMul = ttk.Button(gui, text='*', command=Fun_Mul).place(x=230, y=130)
btnDiv = ttk.Button(gui, text='/', command=Fun_Div).place(x=230, y=160)
btn_clear = ttk.Button(gui, text='Clear', width=17, command=clear_textbox).place(x=130, y=190)


# Call gui
gui.mainloop()

# complese