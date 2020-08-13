
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
from tkinter import *

windows = Tk()
windows.geometry('500x300+900+200')
windows.resizable(0, 0)
windows.config(padx=10, pady=10)




windows.mainloop()







