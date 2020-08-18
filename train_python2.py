# ===== 15/08/2020 =====
# สอน Label Frame[/]
'''
from tkinter import *

windows = Tk()
windows.title('Test Label Frame')
windows.geometry('500x350+900+200')
windows.resizable(0, 0)

# frame 1 ------------
fm1 = LabelFrame(windows, text='ข้อมูลส่วนตัว')
fm1.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)

lbl_name = Label(fm1, text='ชื่อ - นามสกุล')
lbl_name.grid(row=0, column=0, sticky=W, padx=5, pady=5)
txt_name = Entry(fm1, width=35)
txt_name.grid(row=0, column=1, sticky=W, padx=5, pady=5)

lbl_address = Label(fm1, text='ที่อยู่')
lbl_address.grid(row=1, column=0, sticky=W, padx=5, pady=5)
txt_address = Entry(fm1, width=35)
txt_address.grid(row=1, column=1, sticky=W, padx=5, pady=5)

lbl_study = Label(fm1, text='การศึกษาสูงสุด')
lbl_study.grid(row=2, column=0, sticky=W, padx=5, pady=5)
txt_study = Entry(fm1, width=35)
txt_study.grid(row=2, column=1, sticky=W, padx=5, pady=5)

lbl_age = Label(fm1, text='อายุ')
lbl_age.grid(row=3, column=0, sticky=W, padx=5, pady=5)
txt_age = Entry(fm1, width=10)
txt_age.grid(row=3, column=1, sticky=W, padx=5, pady=5)
lbl_age2 = Label(fm1, text='ปี')
lbl_age2.place(x=220, y=121)

# frame 2 ------------
fm2 = LabelFrame(windows, text='ข้อมูลที่ทำงาน')
fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)

lbl_address_work = Label(fm2, text='ที่ทำงาน')
lbl_address_work.grid(row=0, column=0, sticky=W, padx=5, pady=5)
txt_name_work = Entry(fm2, width=35)
txt_name_work.grid(row=0, column=1, sticky=W, padx=5, pady=5)

lbl_position = Label(fm2, text='ตำแหน่ง')
lbl_position.grid(row=1, column=0, sticky=W, padx=5, pady=5)
txt_position = Entry(fm2, width=35)
txt_position.grid(row=1, column=1, sticky=W, padx=5, pady=5)

windows.mainloop()
'''

# สอนสร้าง GUI ทุกๆแบบใน Windows เดียว [/]
'''
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
import sys

# function area
def hello():
    print('Hello Nattapong Ngamphak')

def msg_hello(event):
    status = messagebox.askyesno(title='Question', message='ต้องการออกจากระบบใช่มั้ย')
    if status > 0 :
        sys.exit()

def choose_color(event):
    my_color = colorchooser.askcolor()
    lbl_c = Label(text=my_color).pack()

def open_file(event):
    my_file = filedialog.askopenfile()
    lbl_file = Label(text=my_file).pack()


# create GUI
windows = Tk()
windows.title('All Widget')
windows.geometry('600x600+900+100')
windows.resizable(0, 0)

# Label Area
lbl_name = Label(text='Nattapong Ngamphak', bg="gray", fg="white")
lbl_name.pack(side=TOP, padx=5, pady=5)

# button area
btn_hello = Button(text='Hello', command=hello)
btn_hello.pack(side=TOP, padx=5, pady=5)

btn_msg_hello = Button(text='msg_hello')
btn_msg_hello.bind('<Button-1>', msg_hello)
btn_msg_hello.pack(side=TOP, padx=5, pady=5)

btn_color = Button(text='Choose Color')
btn_color.bind('<Button-1>', choose_color)
btn_color.pack(side=TOP, padx=5, pady=5)

btn_file = Button(text='Choose File')
btn_file.bind('<Button-1>', open_file)
btn_file.pack(side=TOP, padx=5, pady=5)

# Create Menu

menu_file = Menu(windows)
file_menu = Menu(menu_file, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open", command=filedialog.askopenfile)
file_menu.add_command(label="Close", command=sys.exit)
menu_file.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menu_file, tearoff=0)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Past")
edit_menu.add_command(label="Delete")
menu_file.add_cascade(label="Edit", menu=edit_menu)

windows.config(menu=menu_file)

# Radio Button
rdo_male = Radiobutton(text='Male', value='male')
rdo_male.pack(side=TOP, padx=5, pady=5)
rdo_female = Radiobutton(text='Female', value='female')
rdo_female.pack(side=TOP, padx=5, pady=5)

# spinbox
spin_box = Spinbox(from_=0, to=10)
spin_box.pack(side=TOP, padx=5, pady=5)

date =['วันจันทร์', 'วันอังคาร', 'วันพุธ', 'วันพฤหัสบดี', 'วันศุกร์', 'วันเสาร์', 'วันอาทิตย์']
spin_box2 = Spinbox(values=date)
spin_box2.pack(side=TOP, padx=5, pady=5)

# listbox
listbox1 = Listbox()
listbox1.insert(1, "Python")
listbox1.insert(2, "Java")
listbox1.insert(3, "Swift")
listbox1.pack(side=TOP, padx=5, pady=5)

# slidebar
slide1 = Scale(orient=HORIZONTAL, width=20, length=300, from_=0, to=100, tickinterval=10)
slide1.pack(side=TOP, padx=5, pady=5)

windows.mainloop()
'''
# สอนเขียน Tkinter แบบ OOP[/]
'''
from tkinter import *

class product:
    def __init__(self, gui):
        self.windows = gui
        self.windows.title('GUI With OOP')
        self.windows.geometry('500x300+900+100')
        self.windows.resizable(0, 0)

        # Frame 1 ==========
        fm1 = LabelFrame(self.windows, text='Product')
        fm1.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)

        self.lbl_product_id = Label(fm1, text='Product_ID')
        self.lbl_product_id.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txt_product_id = Entry(fm1, width=20)
        self.txt_product_id.grid(row=0, column=1, sticky=W, padx=5, pady=5)   

        self.lbl_product_name = Label(fm1, text='Product_name')
        self.lbl_product_name.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txt_product_name = Entry(fm1, width=30)
        self.txt_product_name.grid(row=1, column=1, sticky=W, padx=5, pady=5) 

        # frame 2
        fm2 = LabelFrame(self.windows, text='Price')
        fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)
        self.lbl_product_id2 = Label(fm2, text='Product_ID')
        self.lbl_product_id2.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txt_product_id2 = Entry(fm2, width=20)
        self.txt_product_id2.grid(row=0, column=1, sticky=W, padx=5, pady=5)   

        self.lbl_product_name2 = Label(fm2, text='Product_name')
        self.lbl_product_name2.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txt_product_name2 = Entry(fm2, width=30)
        self.txt_product_name2.grid(row=1, column=1, sticky=W, padx=5, pady=5) 



if __name__ == '__main__':
    gui = Tk()
    application = product(gui)
    gui.mainloop()

'''
# แบบฝึกหัด tkinter โปรแกรมบวกเลข[/]
'''
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys

# function area
def clear_data():
    str_add.set('')
    str_add2.set('')
    str_sum.set('')

def func_add():    
    check_add = str_add.get()
    check_add2 = str_add2.get()
   
    if check_add == '':
        messagebox.showwarning(title='Alert', message='Number is null, please check number')
        return
    
    if check_add2 == '':
        messagebox.showwarning(title='Alert', message='Number is null, please check number')
        return

    read_add = float(str_add.get())
    read_add2 = float(str_add2.get())

    sum = read_add + read_add2
    str_sum.set(sum)

def func_minus():
    check_add = str_add.get()
    check_add2 = str_add2.get()
   
    if check_add == '':
        messagebox.showwarning(title='Alert', message='Number is null, please check number')
        return
    
    if check_add2 == '':
        messagebox.showwarning(title='Alert', message='Number is null, please check number')
        return

    read_add = float(str_add.get())
    read_add2 = float(str_add2.get())

    read_add = float(str_add.get())
    read_add2 = float(str_add2.get())

    sum = read_add - read_add2
    str_sum.set(sum)

def func_mul():
    check_add = str_add.get()
    check_add2 = str_add2.get()
   
    if check_add == '':
        messagebox.showwarning(title='Alert', message='Number is null, please check number')
        return
    
    if check_add2 == '':
        messagebox.showwarning(title='Alert', message='Number is null, please check number')
        return

    read_add = float(str_add.get())
    read_add2 = float(str_add2.get())

    read_add = float(str_add.get())
    read_add2 = float(str_add2.get())

    sum = read_add * read_add2
    str_sum.set(sum)

def func_div():
    check_add = str_add.get()
    check_add2 = str_add2.get()
   
    if check_add == '':
        messagebox.showwarning(title='Alert', message='Number is null, please check number')
        return
    
    if check_add2 == '':
        messagebox.showwarning(title='Alert', message='Number is null, please check number')
        return

    read_add = float(str_add.get())
    read_add2 = float(str_add2.get())

    read_add = float(str_add.get())
    read_add2 = float(str_add2.get())

    sum = read_add / read_add2
    str_sum.set(sum)

# create windows
windows = Tk()
windows.title('Easy Calculator')
windows.geometry('360x250+900+100')
windows.resizable(0, 0)

# create label
lbl_text_show = Label(windows, text='Calculator by Nattapong').pack()
lbl_num_1 = Label(windows, text='Number 1').place(x=20, y=30)
lbl_num_2 = Label(windows, text='Number 2').place(x=20, y=60)
lbl_num_total = Label(windows, text='Total Number').place(x=20, y=90)

# textbox
str_add = StringVar()
str_add2 = StringVar()
str_sum = StringVar()
str_div = StringVar()

txt_number1 = Entry(textvariable=str_add).place(x=130, y=30)
txt_number2 = Entry(textvariable=str_add2).place(x=130, y=60)
txt_number_sum = Entry(textvariable=str_sum, state=DISABLED).place(x=130, y=90)


# Button 
btn_add = ttk.Button(windows, text='+', command=func_add).place(x=130, y=130)
btn_minus = ttk.Button(windows, text='-', command=func_minus).place(x=130, y=160)
btn_mul = ttk.Button(windows, text='x', command=func_mul).place(x=230, y=130)
btn_div = ttk.Button(windows, text='/', command=func_div).place(x=230, y=160)
btn_clear = ttk.Button(windows, text='Clear', width=17, command=clear_data).place(x=130, y=190)


windows.mainloop()

'''
# สอนการใช้งาน GitHub[x]
'''
command use
=== first commit repository
git init
git add README.md
git commit -m '...key word...'
git remote add origin ... URL Git repository ...
git push -u origin master

=== Update repository
git add .
git commit -m '...key word...'
git push -u origin master
'''

# Database SQLite3 [/]
# connect database, show data from database[*]
# เขียน tkinter เชื่อมต่อกับฐานข้อมูล (ตัวอย่างเพิ่ม ลบ แก้ไข ข้อมูลสินค้า) [x]



















