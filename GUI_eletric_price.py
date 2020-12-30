from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas # libarlies for create Dataframe
from datetime import date # libralies datetime for set textbox date
import numpy
import matplotlib.pyplot as plt # libralies for plot grap
import sqlite3 # libralies database
import sys



print(sys.version)
# ---------- connect Database SQLite3 -----------
con = sqlite3.connect('Database/DB_Test.db')
cur = con.cursor()
#-------------- Function -------------------
def clear_data(): # use for button clear 
    ID.set('')
    old_unit.set('')
    now_unit.set('')
    use_unit.set('')
    eletric_price.set('')
    total_price.set('')
 
    set_date() # call function set date for set date to today.
    set_max_old_unit() # call function for set textbox to max old unit.
    # Complese Function ------------

def calculate(): # use for button calculate 
    # คำนวนจำนวนหน่วยที่ใช้งาน
    cal_old_unit = old_unit.get()
    cal_now_unit = now_unit.get()

    
    if cal_old_unit =='':
        messagebox.showwarning(title='Alert', message='Old_Unit is emtry.')
    elif cal_now_unit =='':
        messagebox.showwarning(title='Alert', message='Now Unit is emtry.')
    # ตรวจสอบว่าค่าที่รับเข้ามาเป็นตัวเลขหรือไม่
    elif cal_now_unit.isnumeric() == False:
        messagebox.showwarning(title='Alert', message='Now Unit is not numeric.')
    elif cal_old_unit > cal_now_unit:
        messagebox.showwarning(title='Alert.', message='Old_Unit is more Now_Unit please check data.')
    else:
        use_unit.set(int(cal_now_unit) - int(cal_old_unit))
        # คำนวนค่าไฟโดยนำหน่วยไปคูณค่าไฟแต่ล่ะหน่วย
        cal_use_unit = use_unit.get()
        ele_price = float(int(cal_use_unit)*6)
        eletric_price.set(ele_price)

        cal_eletric_price = float(eletric_price.get())
        total_price.set(float(cal_eletric_price)+200)
    # Complese Function ------------
    
def show_data():
    # Clear data in Treeview if have data
    record = tree.get_children()
    for element in record:
        tree.delete(element)

    # filling data into treeview
    sqlSelect = 'SELECT * FROM Tb_Electric ORDER BY ID DESC'
    rows = con.execute(sqlSelect)
    cpt = 0
    for row_show in rows:
        # print(row_show)
        tree.insert('', 'end', text=str(cpt),
                               values=(row_show[0], row_show[1], row_show[2],
                                       row_show[3], row_show[4], row_show[5], row_show[6]))
        cpt += 1
    
    # call function because when start up write call function show_data olny.
    set_max_id()
    set_max_old_unit()
    set_date()
    # Complese Function ------------
    

def insert_data():
    str_id = ID.get()
    str_date = Date.get()
    str_old_unit = old_unit.get()
    str_now_unit = now_unit.get()
    str_use_unit = use_unit.get()

    if str_id =='':
        messagebox.showwarning(title='Alert', message='ID is missing.')
    elif str_date =='':
        messagebox.showwarning(title='Alert', message='Date is missing.')
    elif str_old_unit =='':
        messagebox.showwarning(title='Alert', message='Old Unit is missing.')
    elif str_now_unit =='':
        messagebox.showwarning(title='Alert', message='Now Unit is missing.')
    elif str_use_unit == '':
        messagebox.showwarning(title='Alert', message='Please click Calculate.')
    else:
        str_eletric_price = float(eletric_price.get())
        str_total_price = float(total_price.get())

         # create message for confirm insert data
        insert_confirm = messagebox.askyesno(title='Confirm save data.', 
                                             message='Are you want to sure insert data?')

        if insert_confirm > 0:
            sql_insert = 'INSERT INTO Tb_Electric VALUES(?,?,?,?,?,?,?);'
            data_insert = [str_id, str_date, str_old_unit, str_now_unit, str_use_unit, 
                str_eletric_price, str_total_price]
            con.execute(sql_insert, data_insert)
            con.commit()
            # call function
            show_data()
            clear_data()
            set_max_id()
        # Complese Function ------------


def update_data():
    update_id = ID.get()
    update_date = Date.get()
    update_old_unit = old_unit.get()
    update_now_unit = now_unit.get()
    update_use_unit = use_unit.get()

    if update_id =='':
        messagebox.showwarning(title='Alert', message='ID is missing.')
    elif update_date =='':
        messagebox.showwarning(title='Alert', message='Date is missing.')
    elif update_old_unit =='':
        messagebox.showwarning(title='Alert', message='Old Unit is missing.')
    elif update_now_unit =='':
        messagebox.showwarning(title='Alert', message='Now Unit is missing.')
    elif update_use_unit == '':
        messagebox.showwarning(title='Alert', message='Please click Calculate.')
    else:
        update_eletric_price = float(eletric_price.get())
        update_total_price = float(total_price.get())

         # create message for confirm insert data
        update_confirm = messagebox.askyesno(title='Confirm update data.', 
                                             message='Are you want to sure update data?')

        if update_confirm > 0:

            sql_update = 'UPDATE Tb_Electric SET Date_Pay=?, Old_Unit=?, Now_Unit=?, Use_Unit=?,'\
                         'Electric_Price=?, Total_Price=? WHERE ID=?;'
            data_update = [update_date, update_old_unit, update_now_unit, update_use_unit,
                           update_eletric_price, update_total_price, update_id]
            con.execute(sql_update, data_update)
            con.commit()
            # call function for refresh
            clear_data()
            show_data()


def delete_data():
    str_delete_id = str(ID.get())
    if str_delete_id =='':
        messagebox.showwarning(title='Alert', message='ID for is null.')
    else:
        # create message for confirm delete data
        confirm_delete = messagebox.askyesno(title='Confirm delete data. ',
                                             message='Are you want to sure delete data ?')
        if confirm_delete > 0 :
            sql_delete = 'DELETE FROM Tb_Electric WHERE ID = ?'
            data_delete = [str_delete_id]
            con.execute(sql_delete, data_delete)
            con.commit()
            #---- call function -----
            clear_data()
            show_data()
            set_max_id()
            # Delete Complease Function can be running.


def select_treeview(event): # create selection in treeview to show in textbok for edit.
    # select in treeview show in textbox
    item = tree.selection()
    for i in item:
        ID.set(tree.item(i, "values")[0])
        Date.set(tree.item(i, "values")[1])
        old_unit.set(tree.item(i, "values")[2])
        now_unit.set(tree.item(i, "values")[3])
        use_unit.set(tree.item(i, "values")[4])
        eletric_price.set(tree.item(i, "values")[5])
        total_price.set(tree.item(i, "values")[6])
        # 0-6 อิงจากจำนวน column ใน treeview
        # Complese Function ------------


def report_summary(): # funcrion for show dataframe and plot grap summary data.
    #messagebox.showinfo(title='Alert', message='Waite for coding.')
    query_sql = pandas.read_sql_query("SELECT Date_Pay,Total_Price FROM Tb_Electric", con)
    df = pandas.DataFrame(query_sql, columns=['Date_Pay', 'Total_Price'])
    #print(df)
    plt.style.use('seaborn') # กำหนด stype
    df.plot(marker='o',markersize=4, x='Date_Pay', y='Total_Price',color='red')
    plt.title("Eletric And Water Price Per Mount") # กำหนด title ให้กราฟ
    plt.ylabel('Price') # กำหนด title ให้จำนวนเงินแกน y
    plt.xticks(rotation='90') # กำหนดแนว Label แกน X ของกราฟ
    plt.subplots_adjust(bottom=0.256) # กำหนดค่า config subplot เช่น ขนาดความสูง กว้าง ของตัวกราฟ
    plt.show()
    # Complese Function ------------


def set_max_old_unit(): # function for select max Unit for set in textbox and calculate
    # select max old unit for set to textbox old unit
    select_max = 'SELECT MAX(Now_Unit)FROM Tb_Electric'
    cur.execute(select_max)
    row = cur.fetchone() # read one data for cursor
    old_unit.set(row[0]) # row[0] is Data if not row[0] or row data is (xxxx,) can not calaulate
    print('Old eletric unit is', row[0]) 
    # Complese Function ------------


def set_max_id(): # function for set auto id in textbox
    select_max_id = 'SELECT MAX(ID)FROM Tb_Electric'
    cur.execute(select_max_id)
    row_max_id = cur.fetchone()
    ID.set(row_max_id[0]+1) # row_max_id[0] is Data if not row_max_id[0] or row_max_id data is (xxxx,) can not insert
    print('Now ID can insert is',row_max_id[0]+1) # Test show data 
    # Complese Function ------------


def set_date(): # function for set auto date into textbox
    # function set txtDate to today.
    day = date.today()
    Date.set(day.strftime('%d/%b/%Y')) # set format date dd-mm-yyyy
    # Complese Function ------------
    # -------------------------------------------------------------------------------

# ------------ Create Form ---------------
eletric = Tk()
eletric.geometry('1100x600+200+100')
eletric.title('Form Eletric Price')
eletric.resizable(0, 0) # Don't able to drag resize windows

# ------ Create Frame -----------

frame_user = ttk.LabelFrame(eletric, text='Eletric Data.', height=550, width=400).place(x=10, y=10)
frame_showdata = ttk.LabelFrame(eletric, text='Show Data', height=550, width=660).place(x=420, y=10)

# create form for User
lbl_id = ttk.Label(text='ID :').place(x=30, y=40)
lbl_date = ttk.Label(text='Date :').place(x=30, y=70)
lbl_old_unit = ttk.Label(text='Old_Unit :').place(x=30, y=100)
lbl_now_unit = ttk.Label(text='Now_Unit :').place(x=30, y=130)
lbl_use_unit = ttk.Label(text='Use Unit :').place(x=30, y=160)
lbl_eletric_price = ttk.Label(text='Eletric_Price :').place(x=30, y=190)
lbl_total_price = ttk.Label(text='Total_Price :').place(x=30, y=220)
lbl_note = ttk.Label(text='# Total Price is Eletric_Price + Water price').place(x=30, y=250)
lbl_note_2 = ttk.Label(text='# (100 per person.)').place(x=30, y=280)


ID = StringVar()
Date = StringVar()
old_unit = StringVar()
now_unit = StringVar()
use_unit = StringVar()
eletric_price = StringVar()
total_price = StringVar()


txt_id = ttk.Entry(textvariable=ID, state=DISABLED, width=10).place(x=53, y=38)
txt_date = ttk.Entry(textvariable=Date,state=DISABLED, width=15).place(x=70, y=67)
txt_old_unit = ttk.Entry(textvariable=old_unit, state=DISABLED, width=10).place(x=93, y=97)
txt_now_unit = ttk.Entry(textvariable=now_unit, width=10).place(x=103, y=127)
txt_use_unit = ttk.Entry(textvariable=use_unit, state=DISABLED, width=10).place(x=105, y=157)
txt_eletric_price = ttk.Entry(textvariable=eletric_price, state=DISABLED, width=10).place(x=115, y=187)
txt_total_price = ttk.Entry(textvariable=total_price, state=DISABLED, width=10).place(x=115, y=217)

# Image for button
img_save = PhotoImage(file="image/save.png")
img_edit = PhotoImage(file="image/edit2.png")
img_delete = PhotoImage(file="image/delete.png")
img_calculate = PhotoImage(file="image/calculate.png")
img_clear = PhotoImage(file="image/clear.png")
img_report = PhotoImage(file="image/report.png")

# create button
btn_save = ttk.Button(eletric, text='Save', image=img_save, compound="top", command=insert_data)\
    .place(width=100, height=100, x=300, y=38)
btn_edit = ttk.Button(text='Edit',image=img_edit, compound="top", command=update_data)\
    .place(width=100, height=100, x=300, y=140)
btn_delete = ttk.Button(text='Delete',image=img_delete, compound='top', command=delete_data)\
    .place(width=100, height=100, x=300, y=240)
btn_clear = ttk.Button(text='Clear',image=img_clear, compound='top', command=clear_data)\
    .place(width=100, height=100, x=300, y=340)
btn_calcilate = ttk.Button(text='Calculate',image=img_calculate, compound='top', command=calculate)\
    .place(width=100, height=100, x=300, y=440)
btn_report = ttk.Button(text='Report',image=img_report, compound='top', command=report_summary)\
    .place(width=100, height=100, x=200, y=440)


# create treeview
tree = ttk.Treeview()
tree['show'] = 'headings'
tree['columns'] = ('ID', 'Date', 'Old_Unit', 'Now_Unit', 'Use_Unit', 'Eletric_Price', 'Total_Price')
tree.heading('ID', text='ID')
tree.heading('Date', text='Date')
tree.heading('Old_Unit', text='Old_Unit')
tree.heading('Now_Unit', text='Now_Unit')
tree.heading('Use_Unit', text='Use_Unit')
tree.heading('Eletric_Price', text='Eletric_Price')
tree.heading('Total_Price', text='Total_Price')
tree.column('ID', width=30)
tree.column('Date', width=100)
tree.column('Old_Unit', width=100)
tree.column('Now_Unit', width=100)
tree.column('Use_Unit', width=100)
tree.column('Eletric_Price', width=100)
tree.column('Total_Price', width=100)
tree.place(height=500, x=430, y=40)
tree.bind('<ButtonRelease>', select_treeview)


# -------- Call eletric windows --------
show_data() # call function 
#set_max_old_unit() # function for set textbox Old Unit
#set_date() # function for set date 
#set_max_id() # function set auto id

eletric.mainloop()




















