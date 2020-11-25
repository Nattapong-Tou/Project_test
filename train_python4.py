'''
โปรแกรมเก็บข้อมูลสินค้า
Requiment
    - ต้องมีฐานข้อมูลเก็บรายละเอียดของสินค้า
        Tb_Product
            ID(Primary Key)
            product_name
            product_price
    - Insert / Update / delete สินค้า
    - ปุ่ม Insert / Update / delete ให้ใส่ภาพ icon เข้าไปด้วย
    - เช็คก่อน insert ห้ามมี textbox เป็นค่าว่าง ให้แจ้งเตือนด้วย Messagebox
    - textbox ราคาสินค้าห้ามกรอกอักษรลงไป ให้แจ้งเตือนด้วย Messagebox
ส่ง [3/9/2020]
'''

'''

import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# connect database
con = sqlite3.connect('database/DB_Train.db')
cur = con.cursor()

# function
# function
def show_data():
    record = tree.get_children()
    for element in record:
        tree.delete(element)

    sql_select = 'SELECT * FROM tb_product'
    rows = con.execute(sql_select)
    cpt = 0
    for rows_show in rows:
        tree.insert('','end', text=str(cpt), values=(rows_show[0], rows_show[1],
                    rows_show[2]))
        cpt += 1
    set_max_id()


def set_max_id():
    sql = 'SELECT MAX(ID) FROM tb_product'
    cur.execute(sql)
    rows_max = cur.fetchone()
    set_id = rows_max[0] + 1
    str_id.set(set_id)


def clear_data():
    str_name.set('')
    str_id.set('')
    str_price.set('')
    
    # call function
    set_max_id()


def select_data(event):
    item = tree.selection()
    for i in item:
        str_id.set(tree.item(i, "values")[0])
        str_name.set(tree.item(i, "values")[1])
        str_price.set(tree.item(i, "values")[2])
       

    
def insert_data():
    id = str_id.get()
    name = str_name.get()
    price = str_price.get()
    

    if id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
    elif name == '':
        messagebox.showwarning(title='Warning', message='Name is missing. !!!')
    elif price == '':
        messagebox.showwarning(title='Warning', message='Price is missing. !!!')     
    elif price.isnumeric() == False:
        messagebox.showwarning(title='Warning', message='Price is not numeric. !!!')
    else:
        insert = messagebox.askyesno(title='Comfirm insert data.', message='Are you want to insert data ?')
        if insert > 0:
            sql_insert = 'INSERT INTO tb_product VALUES(?,?,?);'
            data_insert = [id, name, price]
            con.execute(sql_insert, data_insert)
            con.commit()
            # call function
            show_data()
            clear_data()


def update_data():
    id = str_id.get()
    name = str_name.get()
    price = str_price.get()
   

    if id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
    elif name == '':
        messagebox.showwarning(title='Warning', message='Name is missing. !!!')
    elif price == '':
        messagebox.showwarning(title='Warning', message='Price is missing. !!!')     
    elif price.isnumeric() == False:
        messagebox.showwarning(title='Warning', message='Price is not numeric. !!!')
    else:
        update = messagebox.askyesno(title='Comfirm update data.', message='Are you want to update data ?')
        if update > 0:
            sql_update = 'UPDATE tb_product SET product_name=?, product_price=? WHERE id=?;'
            data_update = [name, price, id]
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
            sql_delete = 'DELETE FROM tb_product WHERE ID=?;'
            data_delete = [id]
            con.execute(sql_delete, data_delete)
            con.commit()
            # call function
            show_data()
            clear_data()

#GUI
windows = Tk()
windows.title('Produce Data')
windows.geometry('600x400+800+100')
windows.resizable(0, 0)

# frame 1
fm1 = LabelFrame(windows, text='User Data', height=150)
fm1.pack(side=TOP, fill=BOTH, padx=10, pady=10)

str_id =StringVar()
str_name = StringVar()
str_price = StringVar()


lbl_id = Label(fm1, text='Product ID :')
lbl_id.grid(row=0, column=0)
txt_id = ttk.Entry(fm1, textvariable=str_id, width=30, state=DISABLED)
txt_id.grid(row=0, column=1)

lbl_name = Label(fm1, text='Product NAME :')
lbl_name.grid(row=1, column=0)
txt_name = ttk.Entry(fm1, textvariable=str_name, width=30)
txt_name.grid(row=1, column=1)

lbl_price = Label(fm1, text='Product Price :')
lbl_price.grid(row=2, column=0)
txt_price = ttk.Entry(fm1, textvariable=str_price, width=30)
txt_price.grid(row=2, column=1)


# create style
style = ttk.Style().configure("BW.TButton", padding=5, relief="flat", background="#99FF33")

btn_insert = ttk.Button(fm1, text='Insert', style='BW.TButton', width=15, command=insert_data)
btn_insert.grid(row=0, column=3, padx=20)
#btn_insert['bg'] = '#E2F8BE'
btn_update = ttk.Button(fm1, text='Update', width=15, command=update_data)
btn_update.grid(row=1, column=3, padx=20)
btn_delete = ttk.Button(fm1, text='Delete', width=15, command=delete_data)
btn_delete.grid(row=2, column=3, padx=20)
btn_clear = ttk.Button(fm1, text='Clear', width=15, command=clear_data)
btn_clear.grid(row=3, column=3, padx=20)
btn_grap = ttk.Button(fm1, text='Show Grap', width=15)
btn_grap.grid(row=4, column=3, padx=20)


# Frame Show data
fm2 = LabelFrame(windows, text='Data')
fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)
tree = ttk.Treeview()
tree['show'] = 'headings'
tree['column'] = ('ID', 'Name', 'Price')
tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Price', text='Price')
tree.column('ID', width=80)
tree.column('Name', width=220)
tree.column('Price', width=220)
tree.place(height=160, x=20, y=220)
tree.bind('<ButtonRelease>', select_data)


show_data()
windows.mainloop()



# 31 /8 /2020
# basic grap with pandas
# pandas 
# numpy = list1D = [1,2,3,4], list2D = [[1,2,3], [4,5,6]] = index(0, 0) = 1, index(1, 0) = 4
# matplotlib

from pandas import *
import numpy 
import matplotlib.pyplot as plt

data = {
    'name': ['Khem', 'Som', 'Tou', 'Boey'],
    'age': [20, 30, 28, 20],
    'gender': ['Male', 'Female', 'Male', 'Male'],
    'money': [20000, 30000, 23000, 20000]
}
# กราฟแบบจุด
df = DataFrame(data)
df.plot(kind='scatter', x='name', y='age', color='red')
plt.show()

# กราฟแบบเส้น
ax = plt.gca()
df.plot(kind='line', x='name', y='age', color='red',ax=ax)
df.plot(kind='line', x='name', y='money', color='blue', ax=ax)
plt.show()


'''


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkmacosx import Button

windows = Tk()
windows.geometry('600x400+800+100')

B1 = Button(windows, text='Mac OSX', bg='black',fg='green', borderless=1)
B1.pack()
B2 = Button(windows, text='Mac OSX', bg='blue',fg='red', borderless=1)
B2.pack()

windows.mainloop()



