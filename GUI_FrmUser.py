from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
from tkinter import messagebox
import sys
gui= Tk()
gui.geometry("500x300+300+200")
gui.title("FormUserDetail.")

# Function for button
def ClearTextBox(event):
    alltext.set(' ')
    Email.set(' ')
    Username.set(' ')
    Password.set(' ')

def messageBoxSave(event):
    attext = str(alltext.get()) # .get() is a pulling data out from box
    messagebox.showinfo(title="Alert", message=attext)
    '''
    txtName.delete(1.0, END)
    txtPAssword.delete(1.0 , END)
    txtUsername.delete(1.0 , END)
    '''

def TestBtnSave(event):
    print("Test")

# Create Label
lblName = Label(gui, text="FirstName - Lastname")
lblName.grid(row=0, column=0)
lblSex = Label(text="Sex")
lblSex.grid(row=1, column=0)
lblBirthday = Label(text="Birthday")
lblBirthday.grid(row=2, column=0)
lblEmail = Label(text="Email")
lblEmail.grid(row=3, column=0)
lblUsername = Label(text="Username")
lblUsername.grid(row=4, column=0)
lblPassword = Label(text="Password")
lblPassword.grid(row=5, column=0)

#Create Textbox
# StringVar สำหรับเก็บค่าใน textbox เพื่อนำไปดำเนินการไม่สามารถตั้งเป็นชื่อเดียวกับ textbox ได้
alltext = StringVar()
Email = StringVar()
Username = StringVar()
Password = StringVar()

ttk.Entry(gui, textvariable=alltext, width=30).grid(row=0, column=1)
ttk.Entry(gui, textvariable=Email, width=30).grid(row=3, column=1)
Entry(gui, textvariable=Username, width=15).place(x=145, y=102)
ttk.Entry(gui, textvariable=Password, width=15).place(x=145, y=128)


# Create Radio Button
rdoMale = ttk.Radiobutton(text="Male", value="Male")\
    .place(x=145, y=28) # วางตามแนวแกน x และ y
rdoFemale = ttk.Radiobutton(text="Female", value="Female")\
    .place(x=220, y=28) # วางตามแนวแกน x และ y
rdoOther = ttk.Radiobutton(text="Other", value="Other")\
    .place(x=300, y=28) # วางตามแนวแกน x และ y

# Create spinbox เพื่อเลือกวัน เดือน ปีเกิด
day = ['จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์','อาทิตย์']
month = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤภาคม','มิถุนายน','กรกฏาคม',
         'สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคท']
year =['2535','2536','2537','2538','2538','2540','2541','2542','2543','2544']

#spDate = Spinbox(value=day, width=7).place(x=145, y=49)
#spMonth = Spinbox(value=month, width=10).place(x=240, y=49)
#spYear = Spinbox(from_=2530, to=2562, width=7).place(x=340, y=49)

# Create combobox
cboDay = ttk.Combobox(value=day, width=7).place(x=145, y=49)
cboMonth = ttk.Combobox(value=month, width=10).place(x=240, y=49)
cboYear = ttk.Combobox(value=year, width=7).place(x=360, y=49)

# Create Listbox
'''
listMonth = Listbox()
listMonth.insert(1,"มกราคม")
listMonth.place(x=180, y=49)
'''

# Create Button
btnClear = Button(text="Clear", width=10, border=2,)
btnClear.bind('<Button-1>', ClearTextBox)
btnClear.place(x=145, y=165)
btnSave = Button(text="Save", width=10, border=2)
btnSave.bind('<Button-1>', messageBoxSave)
btnSave.place(x=250, y=165)

# Call Mainloop For show Form
gui.mainloop()