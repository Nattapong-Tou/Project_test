from tkinter import *
from PIL import Image, ImageTk

# ทดสอบการเรียกภาพ
# Create From
win = Tk()
win.option_add("Font","consolas 20")
img = Image.open("image/py1.jpg")

ShowImg = ImageTk.PhotoImage(img)
lblImage = Label(image=ShowImg).pack()
lblText = Label(win, text="ทดสอบภาพอ้วนๆ").pack()




win.mainloop()
