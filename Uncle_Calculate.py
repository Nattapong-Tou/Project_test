from tkinter import *
from tkinter import ttk  # import liberry ย่อยเพื่อจัดการ Theme
from tkinter import messagebox
from PIL import Image,ImageTk
import sys

# Create Function
def calculate_profit():
    at=int(alltxt.get()) # .get() is a pulling data out from box
    cal_sell = at*30
    cal_cost = at*20
    profit = cal_sell - cal_cost
    rolex = (profit*1000000) / 350000
    # showtext = 'I have profit :',format(profit),'\n'
    # showtext2 = 'I buy rolex : ',format(rolex,',0f')
    # print(profit+rolex)
    # messagebox.showinfo(title='My Profit', message=showText)

    messagebox.showinfo(title='My Profit', message=f'I have profit : {profit} million\n'
                                                  f'and buy rolex : {rolex} pise')



#create frame GUI
gui = Tk()
gui.geometry("400x500+200+200") # +200+200 คือกำหนดหน้าต่างเวลาเปิดว่าให้อยู่ด้านไหนของจอ
gui.title("Uncle Engineer Calculator")

# Create Label
lblCalTang = ttk.Label(text='Program for Calculate Tang Price.').pack(padx=10)

# Create textbox
alltxt = StringVar()
txtcal = ttk.Entry(gui, textvariable=alltxt).pack(padx=10)

# Create Button
btnCal = ttk.Button(gui, text='calculator', command=calculate_profit)\
    .pack(ipadx=5, ipady=5) # ipadx คือระยะห่างตัวหนังสือจากขอบ Button

# set properties button (Add ttk)
#btnCal2 = ttk.Button(gui, text='calculator2').pack()

# Show Image Create Label
imgTank = Image.open("image/tank.jpg")
showTank = ImageTk.PhotoImage(imgTank)
lblTank = ttk.Label(image=showTank).pack()

# call mainloop
gui.mainloop()

# ****************** Complese *******************