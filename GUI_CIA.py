from tkinter import *

#color code
bg='#1c1c1c' #background
fg='#e6e6e6' #foreground

#ทดสอบการสร้างหน้า User Interface แบบ CIA
GUI = Tk()
GUI.geometry('1440x900+900+50') # ปรับขนาดหน้าจอตามที่เราต้องการ
GUI.configure(background=bg) # ปรับสีของพื้นหลัง
#GUI.attributes('-fullscreen', True) # ขยายหน้่าจอให้เต็มจอ

# กำหนดขนาดหน้า GUI ตาม resolution ของเครื่องต่างๆ
windows_width = GUI.winfo_screenwidth()
windows_height = GUI.winfo_screenheight()
print(windows_width, windows_height)
 
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


# --------- Left Zone ----------
# main
FrameRect(50,50,700,700) # from top left corner
FrameRect(50,50,700,20, fill=True) # header bar
# in right
FrameRect(400,85,340,300)

# --------- Right Zone ----------
# main
FrameRect(760,50,640,700) # from top left corner
FrameRect(760,50,640,20, fill=True) # header bar

GUI.mainloop()
 