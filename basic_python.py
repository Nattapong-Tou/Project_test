
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
