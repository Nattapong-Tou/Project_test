# Noteboot Tap
'''
Tap 1
    ข้อมูลสินค้า เพิ่ม, ลบ, แก้ไข ย้ายจากครั้งมาใส่

Tap 2 
    หน้าทดลองการขายสิ้นค้า, ตัด stock


'''

import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# connect database
con = sqlite3.connect('database/DB_Train.db')
cur = con.cursor()

# Function area
# Function Tap Product Data

def show_data():
    record = tree.get_children()
    for element in record:
        tree.delete(element)

    sql_select = 'SELECT * FROM tb_product'
    rows = con.execute(sql_select)
    cpt = 0
    for rows_show in rows:
        tree.insert('','end', text=str(cpt), values=(rows_show[0], rows_show[1],
                    rows_show[2], rows_show[3]))
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
    str_amount.set('')
    
    # call function
    set_max_id()


def select_data(event):
    item = tree.selection()
    for i in item:
        str_id.set(tree.item(i, "values")[0])
        str_name.set(tree.item(i, "values")[1])
        str_price.set(tree.item(i, "values")[2])
        str_amount.set(tree.item(i, "values")[3])
       
    
def insert_data():
    id = str_id.get()
    name = str_name.get()
    price = str_price.get()
    amount = str_amount.get()

    if id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
    elif name == '':
        messagebox.showwarning(title='Warning', message='Name is missing. !!!')
    elif price == '':
        messagebox.showwarning(title='Warning', message='Price is missing. !!!')     
    elif price.isnumeric() == False:
        messagebox.showwarning(title='Warning', message='Price is not numeric. !!!')
    elif amount == '':
        messagebox.showwarning(title='Warning', message='Amount is missing. !!!')     
    elif amount.isnumeric() == False:
        messagebox.showwarning(title='Warning', message='Amount is not numeric. !!!')
    else:
        insert = messagebox.askyesno(title='Comfirm insert data.', message='Are you want to insert data ?')
        if insert > 0:
            sql_insert = 'INSERT INTO tb_product VALUES(?,?,?,?);'
            data_insert = [id, name, price, amount]
            con.execute(sql_insert, data_insert)
            con.commit()
            # call function
            show_data()
            clear_data()


def update_data():
    id = str_id.get()
    name = str_name.get()
    price = str_price.get()
    amount = str_amount.get()

    if id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
    elif name == '':
        messagebox.showwarning(title='Warning', message='Name is missing. !!!')
    elif price == '':
        messagebox.showwarning(title='Warning', message='Price is missing. !!!')     
    elif price.isnumeric() == False:
        messagebox.showwarning(title='Warning', message='Price is not numeric. !!!')
    elif amount == '':
        messagebox.showwarning(title='Warning', message='amount is missing. !!!')     
    elif amount.isnumeric() == False:
        messagebox.showwarning(title='Warning', message='amount is not numeric. !!!')
    else:
        update = messagebox.askyesno(title='Comfirm update data.', message='Are you want to update data ?')
        if update > 0:
            sql_update = 'UPDATE tb_product SET product_name=?, product_price=?, amount=? WHERE id=?;'
            data_update = [name, price, amount, id]
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

# windows form area
windows = Tk()
windows.geometry('700x500+700+150')
windows.resizable(0,0)
windows.title('Program Product')

# create Notebook
notebook = ttk.Notebook(windows, width=660, height=460)
notebook.pack(padx=5, pady=5)

# create Frame
fm_tap1 = Frame(notebook)
fm_tap2 = Frame(notebook)

# add tap
notebook.add(fm_tap1, text='Product Data')
notebook.add(fm_tap2, text='Sale Data')

# create widget in tap
# tap Product Data
str_id =StringVar()
str_name = StringVar()
str_price = StringVar()
str_amount = StringVar()


lbl_id = Label(fm_tap1, text='Product ID :')
lbl_id.grid(row=0, column=0)
txt_id = ttk.Entry(fm_tap1, textvariable=str_id, width=30, state=DISABLED)
txt_id.grid(row=0, column=1)

lbl_name = Label(fm_tap1, text='Product Name :')
lbl_name.grid(row=1, column=0)
txt_name = ttk.Entry(fm_tap1, textvariable=str_name, width=30)
txt_name.grid(row=1, column=1)

lbl_price = Label(fm_tap1, text='Product Price :')
lbl_price.grid(row=2, column=0)
txt_price = ttk.Entry(fm_tap1, textvariable=str_price, width=30)
txt_price.grid(row=2, column=1)

lbl_amount = Label(fm_tap1, text='Amount :')
lbl_amount.grid(row=3, column=0)
txt_amount = ttk.Entry(fm_tap1, textvariable=str_amount, width=30)
txt_amount.grid(row=3, column=1)

# create style
style = ttk.Style().configure("BW.TButton", padding=5, relief="flat", background="#000000")

btn_insert = ttk.Button(fm_tap1, text='Insert', width=15, command=insert_data)
btn_insert.grid(row=0, column=3, padx=20)
#btn_insert['bg'] = '#E2F8BE'
btn_update = ttk.Button(fm_tap1, text='Update', width=15, command=update_data)
btn_update.grid(row=1, column=3, padx=20)

btn_delete = ttk.Button(fm_tap1, text='Delete', width=15, command=delete_data)
btn_delete.grid(row=2, column=3, padx=20)

btn_clear = ttk.Button(fm_tap1, text='Clear', width=15, command=clear_data)
btn_clear.grid(row=3, column=3, padx=20)

btn_grap = ttk.Button(fm_tap1, text='Show Grap', width=15)
btn_grap.grid(row=4, column=3, padx=20)

tree = ttk.Treeview(fm_tap1)
tree['show'] = 'headings'
tree['column'] = ('ID', 'Name', 'Price', 'Amount')
tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Price', text='Price')
tree.heading('Amount', text='Amount')
tree.column('ID', width=80)
tree.column('Name', width=260)
tree.column('Price', width=160)
tree.column('Amount', width=110)
tree.place(height=200, x=15, y=150)
tree.bind('<ButtonRelease>', select_data)

# tap Product Data
str_sale_id = StringVar()

lbl_id_tap2 = Label(fm_tap2, text='ID :')
lbl_id_tap2.grid(row=0, column=0, padx=5, pady=10)


# call function tap Product Data
show_data()

windows.mainloop()





