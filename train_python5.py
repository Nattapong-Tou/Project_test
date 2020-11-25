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
from datetime import date
import sys


# connect database
con = sqlite3.connect('database/DB_Train.db')
cur = con.cursor()

# Function area
# Function Tap Product Data

def show_data():
    record = tree.get_children()
    for element in record:
        tree.delete(element)

    sql_select = 'SELECT * '\
        'FROM tb_product'
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
    show_data()


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

# Function Tap Sale Data
def show_data_sale():
    record = tree_tap2.get_children()
    for element in record:
        tree_tap2.delete(element)

    sql_select = 'SELECT tb_sale.sale_id,tb_order.order_id,tb_order.order_date,tb_product.id,tb_product.product_name,'\
        'tb_sale.total_amount,tb_sale.price,tb_sale.total_price,tb_sale.pay_in,tb_sale.pay_out,tb_sale.cus_id'\
        ' FROM tb_order,tb_product,tb_sale'\
        ' WHERE tb_order.order_id = tb_sale.order_id'\
        ' AND tb_sale.product_id = tb_product.id'

    rows = con.execute(sql_select)
    cpt = 0
    for rows_show in rows:
        tree_tap2.insert('','end', text=str(cpt), values=(rows_show[0], rows_show[1],
                    rows_show[2], rows_show[3], rows_show[4], rows_show[5], rows_show[6],
                    rows_show[7], rows_show[8], rows_show[9], rows_show[10]))
        cpt += 1
    
    # call function when start up
    #set_max_id_order()
    set_max_id_sale()


def clear_data_sale():
    #str_sale_id.set('')
    str_product_id.set('')
    #str_order_id.set('')
    str_cus_id.set('')
    str_amount_sale.set('')
    str_sale_price.set('')
    str_sale_total_price.set('')
    str_sale_pay_in.set('')
    str_sale_pay_out.set('')
    str_sale_date.set('')
    str_amount_sale.set('0')
    str_sale_price.set('0')

    # call function
    #set_max_id_order()
    set_max_id_sale()
    set_date()


def select_data_sale(event):
    item_sale = tree_tap2.selection()
    for i in item_sale:
        str_sale_id.set(tree_tap2.item(i, "values")[0])
        str_order_id.set(tree_tap2.item(i, "values")[1])
        str_sale_date.set(tree_tap2.item(i, "values")[2])
        str_product_id.set(tree_tap2.item(i, "values")[3])
        str_amount_sale.set(tree_tap2.item(i, "values")[5])
        str_sale_price.set(tree_tap2.item(i, "values")[6])
        str_sale_total_price.set(tree_tap2.item(i, "values")[7])
        str_sale_pay_in.set(tree_tap2.item(i, "values")[8])
        str_sale_pay_out.set(tree_tap2.item(i, "values")[9])
        str_cus_id.set(tree_tap2.item(i, "values")[10])


def insert_data_sale():
    sale_id = str_sale_id.get()
    priduct_id = str_product_id.get()
    order_id = str_order_id.get()
    cus_id = str_cus_id.get()
    amount_sale = str_amount_sale.get()
    sale_price = str_sale_price.get()
    sale_total_price = str_sale_total_price.get()
    sale_pay_in = str_sale_pay_in.get()
    sale_pay_out = str_sale_pay_out.get()
    sale_date = str_sale_date.get()

    if sale_id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
    elif priduct_id == '':
        messagebox.showwarning(title='Warning', message='product id is missing. !!!')
    elif order_id == '':
        messagebox.showwarning(title='Warning', message='order id is missing. !!!')
    elif cus_id == '':
        messagebox.showwarning(title='Warning', message='customer id is missing. !!!')
    elif amount_sale == '':
        messagebox.showwarning(title='Warning', message='amount is missing. !!!')
    elif sale_price == '':
        messagebox.showwarning(title='Warning', message='sale price is missing. !!!')
    elif sale_total_price == '':
        messagebox.showwarning(title='Warning', message='total price is missing. !!!')
    elif str_sale_pay_in == '':
        messagebox.showwarning(title='Warning', message='pay in is missing. !!!')
    elif sale_pay_out == '':
        messagebox.showwarning(title='Warning', message='pay out is missing. !!!')
    elif sale_date == '':
        messagebox.showwarning(title='Warning', message='sale date is missing. !!!')
    else:
        insert = messagebox.askyesno(title='Comfirm insert data.', message='Are you want to insert data ?')
        if insert > 0:
            # insert to tb_sale
            sql_insert = 'INSERT INTO tb_sale VALUES(?,?,?,?,?,?,?,?,?);'
            data_insert = [sale_id, priduct_id, order_id, amount_sale, sale_total_price, \
                sale_pay_in, sale_pay_out, sale_price, cus_id]
            con.execute(sql_insert, data_insert)
            con.commit()
 
            # insert to tb_order
            sql_insert_order = 'INSERT INTO tb_order VALUES(?,?);'
            data_insert_order = [order_id, sale_date]
            con.execute(sql_insert_order, data_insert_order)
            con.commit()
            
            # update amount in tb_product
            sql_update_amount = 'UPDATE tb_product SET amount = amount-? WHERE id=?;'
            data_update_amount = [amount_sale, priduct_id]
            con.execute(sql_update_amount, data_update_amount)
            con.commit()

            # call function
            show_data_sale()
            clear_data_sale()


def delete_data_sale():
    sale_id = str_sale_id.get()
    order_id = str_order_id.get()

    if sale_id == '':
        messagebox.showwarning(title='Warning', message='sale id is missing. !!!')
    elif order_id == '':
        messagebox.showwarning(title='Warning', message='order id is missing. !!!')
    else:

        delete = messagebox.askyesno(title='Comfirm delete data.', message='Are you want to delete data ?')
        if delete > 0:
            sql_delete = 'DELETE FROM tb_sale WHERE sale_id=?;'
            data_delete = [sale_id]
            con.execute(sql_delete, data_delete)
            con.commit()

            # delete tb_order
            sql_delete_order = 'DELETE FROM tb_order WHERE order_id=?;'
            data_delete_order = [order_id]
            con.execute(sql_delete_order, data_delete_order)
            con.commit()

            # update amount in tb_product
            sql_update_amount = 'UPDATE tb_product SET amount = amount+? WHERE id=?;'
            data_update_amount = [amount_sale, priduct_id]
            con.execute(sql_update_amount, data_update_amount)
            con.commit()

            # call function
            show_data_sale()
            clear_data_sale()


def set_max_id_sale(): #function ตั้ง sale id แบบ auto
    sql = 'SELECT MAX(sale_id) FROM tb_sale'
    cur.execute(sql)
    rows_max = cur.fetchone()
    set_id = rows_max[0] + 1
    str_sale_id.set(set_id)


def set_max_id_order(): #function ตั้ง order id แบบ auto
    sql = 'SELECT MAX(order_id) FROM tb_order'
    cur.execute(sql)
    rows_max = cur.fetchone()
    set_id = rows_max[0] + 1
    str_order_id.set(set_id)


def calculate_sale(): # function คำนวนเงินทอน
    check_pay_in = str_sale_pay_in.get()
    if check_pay_in == '':
        messagebox.showwarning(title='Warning', message='pay in is missing. !!!')
    else:
        r = float(str_sale_pay_in.get()) - float(str_sale_total_price.get())
        str_sale_pay_out.set(r)


def auto_calculate(*args): #function คำนวนราคาสินค่าแบบ auto    
    r = float(str_amount_sale.get()) * float(str_sale_price.get())
    str_sale_total_price.set(r)


def set_date(): # function สร้างวันที่ใน textbox แบบ auto
    day = date.today()
    str_sale_date.set(day.strftime('%d/%b/%Y')) # format dd-mm-yyyy



# windows form area
windows = Tk()
windows.geometry('1000x500+400+50')
windows.resizable(0,0)
windows.title('Program Product')

# create Notebook
notebook = ttk.Notebook(windows, width=960, height=460)
notebook.pack(padx=5, pady=5)

# create Frame
fm_tap1 = Frame(notebook)
fm_tap2 = Frame(notebook)

# add tap
notebook.add(fm_tap1, text='Product Data')
notebook.add(fm_tap2, text='Sale')

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

# tap sale
str_sale_id = StringVar()
str_product_id = StringVar()
str_order_id = StringVar()
str_cus_id = StringVar()
str_amount_sale = StringVar()
str_sale_price = StringVar()
str_sale_total_price = StringVar()
str_sale_pay_in = StringVar()
str_sale_pay_out = StringVar()
str_sale_date = StringVar()

# calculate แบบ auto ต้องประกาศตัวแปรเพิ่ม
str_amount_sale.set('0')
str_sale_price.set('0')
str_amount_sale.trace_add('write', auto_calculate)
str_sale_price.trace_add('write', auto_calculate)


lbl_id_tap2 = Label(fm_tap2, text='Sale ID :')
lbl_id_tap2.grid(row=0, column=0, padx=5, pady=10)
txt_sale_id = ttk.Entry(fm_tap2, textvariable=str_sale_id, width=10, state=DISABLED)
txt_sale_id.grid(row=0, column=1)

lbl_productid_tap2 = Label(fm_tap2, text='Product ID :')
lbl_productid_tap2.grid(row=0, column=2, padx=5, pady=10)
txt_product_id = ttk.Entry(fm_tap2, textvariable=str_product_id, width=10)
txt_product_id.grid(row=0, column=3)

lbl_order_id = Label(fm_tap2, text='Order ID :')
lbl_order_id.grid(row=0, column=4, padx=5, pady=10)
txt_order_id = ttk.Entry(fm_tap2, textvariable=str_order_id, width=10, state=DISABLED)
txt_order_id.grid(row=0, column=5)

lbl_cus_id = Label(fm_tap2, text='Cus ID :')
lbl_cus_id.grid(row=2, column=4, padx=5, pady=10)
txt_cus_id = ttk.Entry(fm_tap2, textvariable=str_cus_id, width=10)
txt_cus_id.grid(row=2, column=5)

lbl_amount_sale = Label(fm_tap2, text='Amount :')
lbl_amount_sale.grid(row=1, column=0)
txt_amount_sale = ttk.Entry(fm_tap2, textvariable=str_amount_sale, width=10)
txt_amount_sale.grid(row=1, column=1)

lbl_sale_price = Label(fm_tap2, text='Price :')
lbl_sale_price.grid(row=1, column=2)
txt_sale_price = ttk.Entry(fm_tap2, textvariable=str_sale_price, width=10)
txt_sale_price.grid(row=1, column=3)

lbl_sale_total_price = Label(fm_tap2, text='Total Price :')
lbl_sale_total_price.grid(row=1, column=4)
txt_sale_total_price = ttk.Entry(fm_tap2, textvariable=str_sale_total_price, width=10, state=DISABLED)
txt_sale_total_price.grid(row=1, column=5)

lbl_pay_in = Label(fm_tap2, text='Pay In :')
lbl_pay_in.grid(row=2, column=0, padx=5, pady=10)
txt_pay_in = ttk.Entry(fm_tap2, textvariable=str_sale_pay_in, width=10)
txt_pay_in.grid(row=2, column=1)

lbl_pay_out = Label(fm_tap2, text='Pay Out :')
lbl_pay_out.grid(row=2, column=2, padx=5, pady=10)
txt_pay_out = ttk.Entry(fm_tap2, textvariable=str_sale_pay_out, width=10, state=DISABLED)
txt_pay_out.grid(row=2, column=3)

lbl_sale_date = Label(fm_tap2, text='Date :')
lbl_sale_date.grid(row=3, column=0)
txt_sale_date = ttk.Entry(fm_tap2, textvariable=str_sale_date, width=10, state=DISABLED)
txt_sale_date.grid(row=3, column=1)

# image for button
img_sale_insert = PhotoImage(file="image/insert16.png")
img_sale_update = PhotoImage(file="image/update16.png")
img_sale_delete = PhotoImage(file="image/delete16.png")
img_sale_calcu = PhotoImage(file="image/calcu16.png")
img_sale_refresh = PhotoImage(file="image/refresh16.png")

btn_insert_sale = ttk.Button(fm_tap2, text='Insert', image=img_sale_insert, compound="left" \
    ,width=10, command=insert_data_sale)
btn_insert_sale.grid(row=0, column=8, padx=40)
#btn_insert['bg'] = '#E2F8BE'
'''
btn_update_sale = ttk.Button(fm_tap2, text='Update', image=img_sale_update, compound="left" \
    ,width=10, command='')
btn_update_sale.grid(row=1, column=8)
'''
btn_delete_sale = ttk.Button(fm_tap2, text='Delete', image=img_sale_delete, compound="left" \
    ,width=10, command=delete_data_sale)
btn_delete_sale.grid(row=1, column=8)

btn_cal_sale = ttk.Button(fm_tap2, text='Calculate', image=img_sale_calcu, compound="left" \
    ,width=10, command=calculate_sale)
btn_cal_sale.grid(row=2, column=8)

btn_clear_sale = ttk.Button(fm_tap2, text='Clear', image=img_sale_refresh, compound="left" \
    ,width=10, command=clear_data_sale)
btn_clear_sale.grid(row=3, column=8)

btn_success_sale = ttk.Button(fm_tap2, text='Success', image=img_sale_refresh, compound="left" \
    ,width=10, command=set_max_id_order)
btn_success_sale.grid(row=4, column=8, pady=5)

tree_tap2 = ttk.Treeview(fm_tap2)
tree_tap2['show'] = 'headings'
tree_tap2['column'] = ('sale_id', 'order_id', 'Date', 'p_id', 'p_name', 'Amount', 'Price', 't_ptice', 'pay_in', 'pay_out', 'cus_id')
tree_tap2.heading('sale_id', text='sale_id')
tree_tap2.heading('order_id', text='order_id')
tree_tap2.heading('Date', text='Date')
tree_tap2.heading('p_id', text='p_id')
tree_tap2.heading('p_name', text='p_name')
tree_tap2.heading('Amount', text='Amount')
tree_tap2.heading('Price', text='Price')
tree_tap2.heading('t_ptice', text='t_ptice')
tree_tap2.heading('pay_in', text='pay_in')
tree_tap2.heading('pay_out', text='pay_out')
tree_tap2.heading('cus_id', text='cus_id')
tree_tap2.column('sale_id', width=50)
tree_tap2.column('order_id', width=50)
tree_tap2.column('Date', width=100)
tree_tap2.column('p_id', width=50)
tree_tap2.column('p_name', width=150)
tree_tap2.column('Amount', width=70)
tree_tap2.column('Price', width=80)
tree_tap2.column('t_ptice', width=80)
tree_tap2.column('pay_in', width=80)
tree_tap2.column('pay_out', width=80)
tree_tap2.column('cus_id', width=80)
tree_tap2.place(height=235, x=15, y=180)
tree_tap2.bind('<ButtonRelease>', select_data_sale)

# call function tap Product Data
show_data()

# call function tap Sale Data
show_data_sale()
auto_calculate()
set_date()
set_max_id_order()

windows.mainloop()





