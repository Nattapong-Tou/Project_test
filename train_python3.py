# Database SQLite3 [/]
# connect database, show data from database[*]
# เขียน tkinter เชื่อมต่อกับฐานข้อมูล (ตัวอย่างเพิ่ม ลบ แก้ไข ข้อมูล) [x]

import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# connect database
con = sqlite3.connect('database/DB_Train.db')
cur = con.cursor()

# function
def show_data():
    record = tree.get_children()
    for element in record:
        tree.delete(element)

    sql_select = 'SELECT * FROM Tb_Name'
    rows = con.execute(sql_select)
    cpt = 0
    for rows_show in rows:
        tree.insert('','end', text=str(cpt), values=(rows_show[0], rows_show[1],
                    rows_show[2], rows_show[3], rows_show[4]))
        cpt += 1
    set_max_id()


def set_max_id():
    sql = 'SELECT MAX(ID) FROM Tb_Name'
    cur.execute(sql)
    rows_max = cur.fetchone()
    set_id = rows_max[0] + 1
    str_id.set(set_id)


def clear_data():
    str_name.set('')
    str_address.set('')
    str_birthday.set('')
    str_tel.set('')    
    str_id.set('')
    # call function
    set_max_id()


def select_data(event):
    item = tree.selection()
    for i in item:
        str_id.set(tree.item(i, "values")[0])
        str_name.set(tree.item(i, "values")[1])
        str_address.set(tree.item(i, "values")[2])
        str_birthday.set(tree.item(i, "values")[3])
        str_tel.set(tree.item(i, "values")[4])

    
def insert_data():
    id = str_id.get()
    name = str_name.get()
    address = str_address.get()
    birthday = str_birthday.get()
    tel = str_tel.get()

    if id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
    elif name == '':
        messagebox.showwarning(title='Warning', message='Name is missing. !!!')
    elif address == '':
        messagebox.showwarning(title='Warning', message='Address is missing. !!!')     
    elif birthday == '':
        messagebox.showwarning(title='Warning', message='Birthday is missing. !!!')
    elif tel == '':
        messagebox.showwarning(title='Warning', message='Tel is missing. !!!')
    else:
        insert = messagebox.askyesno(title='Comfirm insert data.', message='Are you want to insert data ?')
        if insert > 0:
            sql_insert = 'INSERT INTO Tb_Name VALUES(?,?,?,?,?);'
            data_insert = [id, name, address, birthday, tel]
            con.execute(sql_insert, data_insert)
            con.commit()
            # call function
            show_data()
            clear_data()


def update_data():
    id = str_id.get()
    name = str_name.get()
    address = str_address.get()
    birthday = str_birthday.get()
    tel = str_tel.get()

    if id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
    elif name == '':
        messagebox.showwarning(title='Warning', message='Name is missing. !!!')
    elif address == '':
        messagebox.showwarning(title='Warning', message='Address is missing. !!!')     
    elif birthday == '':
        messagebox.showwarning(title='Warning', message='Birthday is missing. !!!')
    elif tel == '':
        messagebox.showwarning(title='Warning', message='Tel is missing. !!!')
    else:
        update = messagebox.askyesno(title='Comfirm update data.', message='Are you want to update data ?')
        if update > 0:
            sql_update = 'UPDATE Tb_Name SET Name=?, Address=?, Birthday=?, Tel=? WHERE ID=?;'
            data_update = [name, address, birthday, tel, id]
            con.execute(sql_update, data_update)
            con.commit()
            # call function
            show_data()
            clear_data()


def delete_data():
    id = str_id.get()
    if id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
    else:
        delete = messagebox.askyesno(title='Comfirm delete data.', message='Are you want to delete data ?')
        if delete > 0:
            sql_delete = 'DELETE FROM Tb_Name WHERE ID=?;'
            data_delete = [id]
            con.execute(sql_delete, data_delete)
            con.commit()
            # call function
            show_data()
            clear_data()


#GUI
windows = Tk()
windows.title('User Data')
windows.geometry('600x400+800+100')
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
txt_id = ttk.Entry(fm1, textvariable=str_id, width=30, state=DISABLED)
txt_id.grid(row=0, column=1)

lbl_name = Label(fm1, text='NAME :')
lbl_name.grid(row=1, column=0)
txt_name = ttk.Entry(fm1, textvariable=str_name, width=30)
txt_name.grid(row=1, column=1)

lbl_address = Label(fm1, text='Address :')
lbl_address.grid(row=2, column=0)
txt_address = ttk.Entry(fm1, textvariable=str_address, width=30)
txt_address.grid(row=2, column=1)

lbl_birthday = Label(fm1, text='Birthday :')
lbl_birthday.grid(row=3, column=0)
txt_birthday = ttk.Entry(fm1, textvariable=str_birthday, width=30, )
txt_birthday.grid(row=3, column=1)

lbl_tel = Label(fm1, text='Tel :')
lbl_tel.grid(row=4, column=0)
txt_tel = ttk.Entry(fm1, textvariable=str_tel, width=30)
txt_tel.grid(row=4, column=1, pady=3)

# create style
style = ttk.Style().configure("BW.TButton", padding=5, relief="flat", background="#000000")

btn_insert = ttk.Button(fm1, text='Insert', width=15, command=insert_data)
btn_insert.grid(row=0, column=3, padx=20)
#btn_insert['bg'] = '#E2F8BE'
btn_update = ttk.Button(fm1, text='Update', width=15, command=update_data)
btn_update.grid(row=1, column=3, padx=20)
btn_delete = ttk.Button(fm1, text='Delete', width=15, command=delete_data)
btn_delete.grid(row=2, column=3, padx=20)
btn_clear = ttk.Button(fm1, text='Clear', width=15, command=clear_data)
btn_clear.grid(row=3, column=3, padx=20)


# Frame Show data
fm2 = LabelFrame(windows, text='Data')
fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)
tree = ttk.Treeview()
tree['show'] = 'headings'
tree['column'] = ('ID', 'Name', 'Address', 'Birthday', 'Tel')
tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Address', text='Address')
tree.heading('Birthday', text='birthday')
tree.heading('Tel', text='Tel')
tree.column('ID', width=30)
tree.column('Name', width=150)
tree.column('Address', width=220)
tree.column('Birthday', width=80)
tree.column('Tel', width=80)
tree.place(height=160, x=20, y=220)
tree.bind('<ButtonRelease>', select_data)


show_data()
windows.mainloop()