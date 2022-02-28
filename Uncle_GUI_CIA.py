from tkinter import *
from tkinter import font
import tkinter.scrolledtext as st
from PIL import Image, ImageTk # libraries pillow
import wikipedia


wikipedia.set_lang('th')

#color code
bg='#1c1c1c' #background
fg='#e6e6e6' #foreground

#ทดสอบการสร้างหน้า User Interface แบบ CIA
GUI = Tk()
GUI.title('CIA GUI')
GUI.geometry('1440x900+900+50') # ปรับขนาดหน้าจอตามที่เราต้องการ
GUI.configure(background=bg) # ปรับสีของพื้นหลัง
#GUI.attributes('-fullscreen', True) # ขยายหน้่าจอให้เต็มจอ

# กำหนดขนาดหน้า GUI ตาม resolution ของเครื่องต่างๆ
windows_width = GUI.winfo_screenwidth()
windows_height = GUI.winfo_screenheight()
#print(windows_width, windows_height)
 
canvas = Canvas(GUI, width=windows_width, height=windows_height, background=bg)
canvas.configure(bd=0, relief='ridge', highlightthickness=0) # ทำให้จอไม่มีขอบ
canvas.place(x=0,y=0)

# function for create frame in canvas 
def FrameRect(x, y, width=200, height=200, fill=False):
    if fill: # fill == True
        frame1 = canvas.create_rectangle(0,0,width,height, outline=fg, width=2, fill=fg)
    else:
        frame1 = canvas.create_rectangle(0,0,width,height, outline=fg, width=2)
    canvas.move(frame1,x ,y)


# --------- configuration font ----------
f1 = ('Source Code Pro', 24) #('font name', font size)
f2 = ('Source Code Pro', 14)


# --------- Top Zone ----------
L1 = Label(GUI, text='NATTAPONG USER DATABASE.', bg=bg, fg=fg, font=f1).place(x=45, y=10)

def FixedText(x,y,text='Fixed Text',font=f2,color=fg): # function สำหรับสร้าง Text และ location ของ Text
    L1 = Label(GUI, text=text, bg=bg, fg=color, font=font).place(x=x, y=y)



# --------- Left Zone ----------
# main
FrameRect(50,50,700,700) # from top left corner
FrameRect(50,50,700,30) # header bar
FixedText(355,53,'USER INFO.')

# in right
FrameRect(400,85,340,300)

#img = PhotoImage(file="image/cat.png")
image = Image.open('image/cat.png')# Use Pillow for read(Open) image
image = image.resize((330, 350)) # Use Pillow for resize image 
img = ImageTk.PhotoImage(image) 
user_photo = Label(GUI, image=img, bd=0, relief='ridge', highlightthickness=0).place(x=60, y=85)

# in buttom จะดึงข้อมูงมาจากฐานข้อมูล
v_experience = StringVar()
v_experience.set('-- Experience Result --')

text = wikipedia.summary('Bill Gates') # ดึงข้อมูลของ Bill Gates มาจากเว็บไซต์ wikipedia
v_experience.set(text)

Frame_1 = Frame(GUI, width=335) #กำหนดความกว้างของ frame เพื่อวางข้อความที่ดึงมาจาก wikipedia
Frame_1.place(x=60,y=440)

experience = st.ScrolledText(Frame_1, width=34, height=16, bg=bg, fg=fg, font=f2)
experience.pack()
experience.insert(INSERT, v_experience.get())


'''
experience = Label(Frame_1, textvariable=v_experience, font=f2, fg=fg, bg=bg)
experience.pack()

'''



# --------- Right Zone ----------
# main
FrameRect(760,50,640,700) # from top left corner
FrameRect(760,50,640,30) # header bar

GUI.mainloop()
 