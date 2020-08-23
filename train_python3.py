# Database SQLite3 [/]
# connect database, show data from database[*]
# เขียน tkinter เชื่อมต่อกับฐานข้อมูล (ตัวอย่างเพิ่ม ลบ แก้ไข ข้อมูล) [x]

import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# connect database
con = sqlite3.connect('database/DB_Train.db')
con.cursor()

# function


#GUI
windows = Tk()
windows.title('User Data')
windows.geometry('600x400+900+100')
windows.resizable(0, 0)

# frame 1
fm1 = LabelFrame(windows, text='User Data', height=120)
fm1.pack(side=TOP, fill=BOTH, padx=10, pady=10)

str_id =StringVar()
str_name = StringVar()
str_address = StringVar()
str_birthday = StringVar()
str_tel = StringVar()

lbl_id = Label(fm1, text='ID :')
lbl_id.grid(row=0, column=0)
txt_id = Entry(fm1, width=30)
txt_id.grid(row=0, column=1)

lbl_name = Label(fm1, text='NAME :')
lbl_name.grid(row=1, column=0)
txt_name = Entry(fm1, width=30)
txt_name.grid(row=1, column=1)

lbl_address = Label(fm1, text='Address :')
lbl_address.grid(row=2, column=0)
txt_address = Entry(fm1, width=30)
txt_address.grid(row=2, column=1)

lbl_birthday = Label(fm1, text='Birthday :')
lbl_birthday.grid(row=3, column=0)
txt_birthday = Entry(fm1, width=30)
txt_birthday.grid(row=3, column=1)

lbl_age = Label(fm1, text='Age :')
lbl_age.grid(row=4, column=0)
txt_age = Entry(fm1, width=30)
txt_age.grid(row=4, column=1, pady=3)

# create style
style = ttk.Style().configure("BW.TButton", padding=5, relief="flat", background="#000000")

btn_insert = ttk.Button(fm1, text='Insert', width=15)
btn_insert.grid(row=0, column=3, padx=20)
#btn_insert['bg'] = '#E2F8BE'
btn_update = ttk.Button(fm1, text='Update', width=15)
btn_update.grid(row=1, column=3, padx=20)
btn_delete = ttk.Button(fm1, text='Delete', width=15)
btn_delete.grid(row=2, column=3, padx=20)
btn_clear = ttk.Button(fm1, text='Clear', width=15)
btn_clear.grid(row=3, column=3, padx=20)


# Frame Show data
fm2 = LabelFrame(windows, text='Data')
fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)

windows.mainloop()