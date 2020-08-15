
# Label frame
'''
from tkinter import *

windows = Tk()
windows.title('Test Label Frame')
windows.geometry('500x300+900+200')

# frame 1 ======================
fm1 = LabelFrame(windows, text='ข้อมูลส่วนตัว')
fm1.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)
lbl_name = Label(fm1, text='ชื่อ - นามสกุล')
lbl_name.grid(row=0, column=0, sticky=W, padx=5, pady=5)
txt_name = Entry(fm1, width=40)
txt_name.grid(row=0, column=1, padx=5, pady=5)

lbl_address = Label(fm1, text='ที่อยู่')
lbl_address.grid(row=1, column=0, sticky=SW, padx=5, pady=5)
txt_address = Entry(fm1, width=40)
txt_address.grid(row=1, column=1, padx=5, pady=5)

# frame 2 ======================
fm2 = LabelFrame(windows, text='ข้อมูลส่วนตัว')
fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)
lbl_study = Label(fm2, text='ระดับการศึกษาสูงสุด')
lbl_study.grid(row=0, column=0, sticky=W, padx=5, pady=5)
txt_name_study = Entry(fm2, width=35)
txt_name_study.grid(row=0, column=1, padx=5, pady=5)

lbl_study_name = Label(fm2, text='สถาบัน')
lbl_study_name.grid(row=1, column=0, sticky=W, padx=5, pady=5)
txt_univer = Entry(fm2, width=35)
txt_univer.grid(row=1, column=1, padx=5, pady=5)

windows.mainloop()
'''
# Checkbutton and Radiobutton
'''
from tkinter import *

windows = Tk()
windows.title('Test Label Frame')
windows.geometry('500x300+900+200')

# frame 1 ======================
fm1 = LabelFrame(windows, text='Checkbutton')
fm1.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)
boolvar1 = BooleanVar()
boolvar2 = BooleanVar()
boolvar3 = BooleanVar()
check1 = Checkbutton(fm1, text='ONE', variable=boolvar1)
check1.pack(side=LEFT)
check2 = Checkbutton(fm1, text='TWO', variable=boolvar2)
check2.pack(side=LEFT)
check3 = Checkbutton(fm1, text='THREE', variable=boolvar3)
check3.pack(side=LEFT)

# frame 2 ======================
fm2 = LabelFrame(windows, text='Radiobutton')
fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)
fruit = StringVar()
rdo_1 = Radiobutton(fm2, text='Apple', variable=fruit, value='Apple')
rdo_1.pack(side=LEFT)
rdo_2 = Radiobutton(fm2, text='Mango', variable=fruit, value='Mango')
rdo_2.pack(side=LEFT)
rdo_3 = Radiobutton(fm2, text='Grape', variable=fruit, value='Grape')
rdo_3.pack(side=LEFT)

windows.mainloop()

'''
# Example
# เป็นการสร้างตัวเลือกโดยใช้ Checkbutton and Radiobutton สำหรับกำหนดรูปแบบและขนาดตามลำดับ แล้วนำค่าที่เลือกไปใช้กับ font ของ
# Label โดยการเปลี่ยนแปลงจะเกิดทันทีที่เลือกรายการใดรายการหนึ่ง
'''
from tkinter import *

windows = Tk()
windows.geometry('500x300+900+200')
windows.resizable(0, 0)
windows.config(padx=10, pady=10)

def add_widget(w):
    w.pack(side=LEFT, padx=10)
    w.config(command=lambda : update_font())

# Frame 1 --------------------------
bold_var = BooleanVar()
italic_var = BooleanVar()
underline_var = BooleanVar()

fm1 = LabelFrame(windows, text=' Font Style :')
fm1.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)
add_widget(Checkbutton(fm1, text='Bold', variable=bold_var))
add_widget(Checkbutton(fm1, text='Italic', variable=italic_var))
add_widget(Checkbutton(fm1, text='Underline', variable=underline_var))

# Frame 2 --------------------------
fm2 = LabelFrame(windows, text=' Font Size :')
fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)

size_var = StringVar(value=16)

add_widget(Radiobutton(fm2, text='16', variable=size_var, value=16))
add_widget(Radiobutton(fm2, text='24', variable=size_var, value=24))
add_widget(Radiobutton(fm2, text='36', variable=size_var, value=36))
add_widget(Radiobutton(fm2, text='55', variable=size_var, value=55))

lbl_text = Label(text='Python')
lbl_text.pack(fill=X, pady=10)
lbl_text['bg'] = '#BEF6F8' # ใส่สี background color Label

def update_font():
    b = 'bold' if bold_var.get() == True else ''
    i = 'italic' if italic_var.get() == True else ''
    u = 'underline' if underline_var.get() == True else ''
    s = size_var.get()
    fn = f'time {s} {b} {i} {u}'
    lbl_text.config(font=fn)

windows.mainloop()

'''
# Example ประกอบด้วย combobox 2 อันโดยอันแรกให้แสดงชื่อภาค และ อีกอันจะแสดงรายชื่อจังหวัดที่อยู่ในภาคที่ถูกเลือกจาก combobox แรก

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

windows = Tk()
windows.title('Tkinter')
windows.geometry('500x300+900+200')
windows.resizable(0, 0)

data = {
    'ภาคเหนือ' : ['เชียงใหม่', 'เชียงราย', 'ลำปาง', 'น่าน', '...'],
    'ภาคอีสาน' : ['โคราช', 'ขอนแก่น', 'อุดร', 'อุบล', '...'],
    'ภาคกลาง' : ['สิงห์บุรี', 'อ่างทอง', 'ชัยนาท', 'กรุงเทพ', '...'],
    'ภาคใต้' : ['ภูเก็ต', 'สงขลา', 'ยะลา', 'ปัตตานี', '...']
}

part = []
for p in data.keys():
    part.append(p)

combo_part = ttk.Combobox(values=part)
combo_part.pack(padx=10, pady=15)
combo_part.bind("<<ComboboxSelected>>", lambda e: combo_part_selected())

combo_province = ttk.Combobox().pack(padx=10)
combo_province.bind("<<ComboboxSelected>>", lambda e: combo_province_selected())

def combo_part_selected():
    sel_part = combo_part.get()
    provinces = data[sel_part]
    combo_province.delete(0, END)
    combo_province.config(values=provinces)
    combo_province.current(0)
    combo_province_selected()

def combo_province_selected():
    combo_province.current(0)
    messagebox.showinfo(message=combo_province.get())

combo_part.current(0)
combo_part_selected() 


windows.mainloop()








