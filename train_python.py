
# In python lang apple_mango
# @ $ 12 = ไม่สามารถนำไปตั้งเป็นชื่อตัวแปรได้
# = - * / == >= <= != : Operator in python
# (10+10)+(100+100)


'''
23/7/2020
Example  ทบทวน if - elif - else
    รับค่าตัวเลขจากทาง Keyboard เข้ามาสองครั้งแล้วตรวจสอบว่าเป็นเลขคู่หรือเลยคี่
    ผลลัพธ์   
        จำนวนที่ 1 : 20
        20 : เป็นเลขคู่
        จำนวนที่ 2 : 21
        21 : เป็นเลขคี่

    ** หารเอาเศษ = ตัวตั้ง % ตัวหาร
--- เฉลย Code Example ---
odd = 'เลขคี่'
even = 'เลขคู่'
num1 = int(input('จำนวนที่ 1 : '))
num2 = int(input('จำนวนที่ 2 : '))
num3 = int(input('จำนวนที่ 3 : '))
if num1%2 == 0:
    print(f'{num1} เป็น {even}')
elif num1%2 != 0:
    print(f'{num1} เป็น {odd}')
if num2%2 == 0:
    print(f'{num2} เป็น {even}')
elif num2%2 != 0:
    print(f'{num2} เป็น {odd}')
if num3%2 == 0:
    print(f'{num3} เป็น {even}')
elif num3%2 != 0:
    print(f'{num3} เป็น {odd}')

Homework
ให้รับค่ามาสามค่าแล้วบอกว่าจำนวนไหนมีค่ามากที่สุด
--- Code เฉลยการบ้าน ---
n1 = int(input('จำนวนที่ 1 >> '))
max = n1
n2 = int(input('จำนวนที่ 2 >> '))
if n2 > max:
    max = n2
n3 = int(input('จำนวนที่ 3 >> '))
if n3 > max:
    max = n3
print('จำนวนที่มากที่สุดคือ ', max)


24/7/2020 For loop

syntax
for ตัวแปร in rang (เริ่มต้น, สิ้นสุด, สเต็บ):
    คำสั่งต่างๆ

for i in rang(1,10,2)
    print(i)

หาผลรวมของจำนวน 1 - 10 โดยใช้ For loop
sum = 0
for i in range (1, 11):
    num = i
    sum += num

print(sum)

Example1. ถ้าต้องการหาว่าจำนวน 1-100 มีจำนวนที่ 2 , 4 และ 5 หารลงตัวกี่จำนวน
count = 0 
for i in range(1, 101):
    if (i % 2 == 0) and (i % 5==0):
        count += 1
print('จำนวน 1 - 100 ที่ 2 และ 5 หารลงตัวมีทั้งหมด',count)

Example2. รับค่าเข้ามา 5 ค่าโดยใช้ For จากนั้นหาผลรวมและค่าเฉลี่ย
sum = 0
for i in range(1, 6):
    num = int(input(f'จำนวนที่ {i} :'))
    sum += num

print('ผลรวมทั้งหมดเท่ากับ : ',sum)
print('ค่าเฉลี่ยเท่ากับ : ',sum/5)
'''

'''
27/7/2020
Loop แบบ while
systax
while เงื่อนไข :
    คำสั่งต่างๆ 
   
x = 1
while x <= 10:
    print(x)
    x += 1 

valid_code = False
while valid_code == False : # ถ้าเงื่อนไขเป็นเท็จให้วนต่อไปเรื่อยๆ
    code = input('กรุณาใส่รหัสผ่าน : ')
    if code == '1234':
        valid_code = True # ถ้าข้อมูลที่ input เข้ามาเป็น 1234 ให้ valid_code = True 
print('รหัสผ่านถูกต้อง')

Example สร้างโปรแกรมสุ่มตัวเลข
import random as rd
x = 0
time = 0
# Module random() ค่าจะอยู่ระหว่าง 0 - 1, ถ้าค่าที่ได้น้อยกว่า 0.5 ให้วนต่อไป
while x < 0.5:
    x = rd.random()
    time += 1
print(f'จะต้องสุ่มทั้งหมด {time} ครั้ง เพื่อที่จะได้ค่า X > 0.5')

Eample 2 เขียนโปรแกรมสูตรคูณด้วย For loop
1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 44
5 10 15 20

print('ตารางสูตรคูณ \n**************')
text = ''
for i in range (1, 13): # loop ในแนวตั้ง
    for j in range (1, 11): # loop ในแนวนอน
        if j == 1:
            text += '' # ไม่ต้องเว้นช่องว่างเมื่อเริ่มแถวใหม่
        elif (i * j) <= 10:
            text += '    ' # ถ้าเป็นเป็นเลขตัวเดียวให้เว้น 4 ช่อง
        else:
            text += '   ' # ถ้าเป็นเป็นเลข 2 หลักให้เว้น 2 ช่อง
        text += str(i * j)
    text += '\n'
print(text)

Date & Time
แสดงเวลาปัจจุบัน
from datetime import datetime
from datetime import date
from datetime import time

now = datetime.now()
day = date.today().strftime('%d/%m/%Y')
curtime = datetime.now().time()
print(now)
print(day)
print(curtime)

+++++ 28 / 7 / 2020 ++++++
-- การจัดรูปแบบ Date time --
dt = datetime.now()
wd = 0 if dt.weekday() == 6 else dt.weekday() + 1
day = dt.day
month = dt.month
year = dt.year + 543
h = dt.hour
m = dt.minute
s = dt.second
print(dt)
print(f'วันเวลาแบบสั้น : {day}/{month}/{year}')
print(f'วันเวลาแบบปกติ : {day} / {thai_month[month - 1]} / {year}')

dmy = f'{thai_date[wd]} ที่ {day} {thai_month[month - 1]} {year}'
time = f'{h}:{m}:{s}'
print(f'วันเวลาแบบเต็ม : {dmy} {time}')

-- การหาระยะห่างของวันที่และเวลา --
day1 = date(2020, 1, 1)
day2 = date(2020, 7, 28)
delta = day2 - day1
print(f'Day1 กับ Day2 ห่างกัน {delta} วัน')

day = delta.days # อ่านจำนวนวันออกมาจาก delta
num_month = day // 30 # หาจำนวนเดือน
num_day = day % 30 # หาจำนวนวัน
print(f'วันที่ 1/1/2020 กับวันที่ 28/7/1010 ห่างกัน {num_month} เดือน {num_day} วัน')

# รับวันเกิดเข้ามาผ่าน Input แล้วเขียนโปรแกรมคำนวนอายุจากวันเกิด
birthday = date(1990, 2, 1)
today = date.today()
delta2 = today - birthday
day2 = delta2.days
age = day2 // 365
print(f'อายุ {age} ปี')

+++++ 29 / 7 / 2020 ++++++
---- ส่งการบ้านโปรแกรมนัดวันที่หาหมอ ----
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

thai_date = ['อาทิตย์','จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์']
thai_month = ['มกราคม','กุมพาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฏาคม','สิงหาคม',
              'กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']

dt = date.today()
print(f'วันนี้ตรงกับ : {dt.day} / {dt.month} / {dt.year + 543}')
app_days = int(input('จำนวนวันที่นัดตรวจครั้งต่อไป : '))
delta = timedelta(days = app_days)
next_dt = dt.__add__(delta) #วันที่จะนัดมาครั้งต่อไป
x = 0
if next_dt.weekday() == 5: # ถ้าวันนัดตรงกับวันเสาร์ ให้เพิ่ม(เลื่อน) ไปอีก 2 วัน
    x = 2
elif next_dt.weekday() == 6: # ถ้าวันนัดตรงกับวันอาทิตย์ ให้เพิ่ม(เลื่อน) ไปอีก 1 วัน
    x = 1

delta = timedelta(days=x)
next_dt2 = next_dt.__add__(delta)

d = next_dt2.day
m = next_dt2.month
y = next_dt2.year + 543
# ทำให้ลำดับวันตรงกับลิส
w = 0 if next_dt2.weekday() == 6 else next_dt2.weekday() + 1
print(f'นัดตรวจครั้งต่อไปตรงกับ : วัน {thai_date[w]} ที่ {d} {thai_month[m - 1]} {y}')

---- การจัดรูปแบบเวลาอย่างง่ายโดยใช้ strftime ----
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

dt = date(2020, 7, 29)
day = dt.strftime('%A-%B-%Y')
print(day)

---- Function ----
- Function แบบไม่ส่งค่ากลับ syntax
def ชื่อ function(patamiter):
    คำสั่งต่างๆ
    
def hello():
    print('Hello Nattapong')

hello() # เรียกใช้ Function

- Function แบบส่งค่ากลับ syntax
def ชื่อ function(patamiter):
    คำสั่งต่างๆ
    return ข้อมูลที่จะส่งกลับ

def select_menu():
    print('กรุณาเลือกเมนู')
    menu = input('1: ถอนเงิน, 2: ถามยอด, 3: โอนเงิน, 0: ยกเลิก >> ')
    p = print(menu)
    return  p

select_menu()
'''

# +++++ 30 / 7 / 2020 ++++++
# * Example สร้าง function random ตัวอักษร[/]
'''
import random

def random_a_to_z():
    a = ord('a')
    z = ord('z')
    r = random.randint(a, z)
    return chr(r)

# เรียกใช้ Function แบบเก็บค่าในตัวแปรก่อน
result = random_a_to_z()
print(result)
# เรียกใช้ Function
print(random_a_to_z())
# เรียกใช้ Function แบบหลายครั้งต่อๆ กัน
code = random_a_to_z() + random_a_to_z() + random_a_to_z() + random_a_to_z()
print(code)
'''

# * แบบฝึกหัด ให้เขียน Function ที่ส่งค่าตัวเลขกลับมา 3 ค่า [/]
'''
import random
def random_3_number():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    r = [a, b, c]
    return r

print(random_3_number())
'''

# * แบบฝึกหัด เขียนโปรแกรมออกหวยรางวันที่ 1 เลขหน้า 3 ตัว เลขท้าย 3 ตัว ด้วยวิธีการสุ่มการออกแต่ล่ะรางวัลใช้วิธีเดียวกันแต่ต่างกันที่จำนวนหลัก
# ดังนั้นเราสร้างแค่ function เดียวเพื่อรับจำนวนหลัก [/]
'''
import random
# ส่วนของ Function
def ran_num(length): # length คือค่าจำนวนหลักที่จะถูกส่งเข้าไปใน Function
    result = ''
    for n in range (0, length):
        r = random.randrange(0, 9)
        result += str(r)
    return result
# ส่วนของการแสดงผล
print(
    'รางวัลที่ 1 :', ran_num(6), '\n'
    'รางวัลเลขหน้า 3 ตัว :', ran_num(3), ' ', ran_num(3), '\n'
    'รางวัลเลขท้าย 3 ตัว :', ran_num(3), ' ', ran_num(3), '\n'
    'รางวัลเลขท้าย 2 ตัว :', ran_num(2), '\n',
    end=''
)
'''

# ตัวอย่างการเขียนโปรแกรม ATM แบบง่ายๆ [*]

'''
สมมุติว่าเป็นการฝาก ถอน และแสดงยอดเงินคงเหลือ โดยทีกระบวนการทั้งหมดจะเป็นไปอย่างต่อเนื่องจนกว่า user จะเลือกเมนูยกเลิก
concept
    1. สร้างเลขสุ่ม เพื่อสมมุติว่าเป็นยอดเงินคงเหลือเริ่มแรก
    2. แสดงเมนูให้เลือกว่าจะถอน ฝาก แสดงยิดเงินหรือยกเลิก
        - ถ้าเลือกแสดงยอดก็อ่านค่ามาแสดง
        - ถ้าเลือกยกเลิกให้หยุดทำงาน
        - ถ้าเลือกฝากหรือถอนให้รับข้อมูลเป็นจำนวนเงิน แล้วนำข้อมูลไปดำเนินการ จากนั้นให้แสดงยอดเงินคงเหลือ
    3. หลักการแสดงยอดเงินคงเหลือ ให้นำเมนูกลับมาแสดง และทำไปเรื่อยๆ
CODE ++++
กำหนดส่ง / เฉลยวันที่ 3/8/2020
'''
'''
import random

balance = random.randint(10000, 50000) # สร้างยอดเงินคงเหลือแบบสุ่ม
menu = 1 # จะให้ Menu เป็นตัวแปร Global
amount = 0 # จะให้ amount เป็นตัวแปร Global
# สร้าง Function แรกเมนูเริ่มต้น
def select_menu():
    global menu # ให้ Menu เป็นตัวแปร Global
    print('\n กรุณาเลือกเมนู')
    menu = input('1: ฝาก, 2: ถอน, 3: ถามยอด, 0:ยกเลิก >>')
    # เขียนเงื่อนไขเพื่อตรวจสอบค่า input
    if not menu.isdigit() or int(menu) not in range (1, 4):
        exit(0)
    else:
        menu = int(menu)

    # ตรวจสอบเงื่อนไขที่ป้อนเข้ามาว่าจะดำเนินการอะไร
    if menu in range(1, 3):
        get_amount()
    elif menu == 3: # menu 3 คือถามยอดให้นำยอดมาแสดง
        show_balance()

def get_amount():
    global amount
    a = input('จำนวนเงิน >> ')
    if not a.isdigit():
        print('ต้องระบุเป็นตัวเลขจำนวนเต็ม')
        get_amount()
    else:
        amount = int(a)
        if menu == 1:
            deposit() # เรียก Function deposit มาทำงาน
        elif menu == 2:
            withdraw() # เรียก Function withdraw มาทำงาน

def deposit():
    global balance
    balance += amount
    show_balance()

def withdraw():
    global balance
    if amount <= balance:
        balance -= amount
        show_balance()
    else:
        print('ยอดเงินไม่เพียงพอ')

def show_balance():
    print('ยอดเงินคงเหลือ :', format(balance, ','))
    select_menu()
# ----- test ------
show_balance()
select_menu()
'''


# ===== 3 / 8 / 2020 ===== [/]
# สอนเรื่อง try - exception [/]

# ===== 4 / 8 / 2020 =====
# สอนเรื่องการอ่านเขียนไฟล์ [/]
# แบบฝึกหัดเรื่องอ่านเขียนไฟล์ โปรแกรมบันทึก log ลง text file
'''
from datetime import datetime
print('*** ถ้าต้องการยกเลิก กด <Enter> โดยไม่ต้องใส่ข้อมูล ***')
try:
    with open('file/sample.txt', mode='w+', encoding='utf-8') as logfile:
        while True: 
            data = input('สิ่งที่เกิดในขณะนี้ >> ')
            # print(data)
            if data == '':
                break

            # ตัดเวลาส่วน microsec ออก
            dt = datetime.now().replace(microsecond=0)
            # นำวันเวลาและข้อมูลมาเขียนลงในไฟล์
            #logfile.write(str(dt) + '--', + data + '\n')
            logfile.write(str(dt) + '---' + data + '\n')

except IOError as err:
    print(err)
'''

# การเขียน File
'''
try:
    with open('file/sample.txt', mode='w+', encoding='utf-8') as file:
        file.write('รายชื่อสัตว์ \n')
        file.write('เข้ม 1 \n')
        file.write('CAT \n')
        file.write('DOG \n')

except IOError as err:
    print(err)
else:
    file.close()
'''

# ===== 8/08/2020 =====
# Line Notify with python [*]
# Create line dev account/Generate Token [/]
# create basic notify [/]
'''
import requests

url = 'https://notify-api.line.me/api/notify'
Token ='ic23VahorgzkTy3iP2xZxfuZNsXFgYeiv2XGyJ36N6v'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+Token} 
msg = 'Line Notify with Python, Hello Nattapong'
r = requests.post(url, headers=headers, data={'message':msg})
print(r.text)
'''
# web scraping data and sent it to line notify [*]
# pip3 install bs4
# pip3 install beautifulsoup4
# pip3 install pandas
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

covid_api = 'https://covid19.th-stat.com/api/open/today'
r_covid = requests.get(covid_api)
r_covid.encoding = 'utf-8'

def line_notify_message_covid(message_covid):
    payload_covid = {'message':message_covid}
    return line_notify_covid(payload_covid)

def line_notify_covid(payload_covid):
    url = 'https://notify-api.line.me/api/notify'
    Token ='ic23VahorgzkTy3iP2xZxfuZNsXFgYeiv2XGyJ36N6v'
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+Token} 
    return requests.post(url, headers=headers, data=payload_covid)

def covid_check():
    line_notify_message_covid('จำนวนผู้ติดเชื้อ Covid - 19 ประจำวันที่'
    + str(r_covid.json()['UpdateDate']) + '\n'
    + 'ผู้ป่วยสะสม:' + str(r_covid.json()['Confirmed']) +'\n'
    + 'ผู้ป่วยหายแล้ว:' +str(r_covid.json()['Recovered']) + '\n'
    + 'ผู้ป่วยที่อยู่ รพ.:' +str(r_covid.json()['Hospitalized']) +'\n'
    + 'ผู้ป่วยใหม่:' +str(r_covid.json()['NewConfirmed']) + '\n'
    + 'เสียชีวิต:' +str(r_covid.json()['Deaths'])
    )

covid_check()

'''

# ===== 8/08/2020 =====
# Teach Virtual enveronment [/]
'''
how to Create virtualenv 
    D://progect here / virtualenv .... Name venv..... --- Windows OS
    virtualenv .... Name venv..... --- MAC OS

activate >> source venv/bin/activate -- MAC OS
            .\venv\Script\activate -- Windows OS
install packet >> pip3 install ...packet name... --- MAC OS
                  pip install ...packet name... --- Windows OS
ดู Packet ที่ติดตั้งแล้ว >> pip3 list -- mac os // pip list -- windows os
upgrade venv >> pip3 install -r requiments.txt --updrade
'''

# ==== Home work [สั่ง 9/08/2020] ====
# เขียน script ดึงราคาทองคำประจำวันแล้วให้ส่งแจ้งเตือนเข้า line notify [ส่ง 13/08/2020][*]
# web_url = 'https://www.goldtraders.or.th/default.aspx'
'''
# check ราคาทองแล้วส่งเข้า line notify
# ตรวจสอบราคาทองคำตัวเว็บไม่มี API เราดึงผ่านหน้าเว็บตรงๆ ไม่ต้องใช้รูปแบบ json 
web_url = 'https://www.goldtraders.or.th/default.aspx'
r = requests.get(web_url)
r.encoding = 'utf-8'
sub = BeautifulSoup(r.text)


def line_notify_message(message):
    payload = {'message':message}
    return line_notify(payload)

def line_notify(payload, file=None):
    URL = 'https://notify-api.line.me/api/notify'
    Token ='ic23VahorgzkTy3iP2xZxfuZNsXFgYeiv2XGyJ36N6v'
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+Token}     
    return requests.post(URL, headers=headers, data=payload, files=file) 

def gold_price_check():
    line_notify_message('ราคาทองคำ 96.5% ประจำวันที่'
        + sub.find(id='DetailPlace_uc_goldprices1_lblAsTime').text + '\n'
        + 'ทองคำแท่ง' + '\n'
        + 'ขายออก : ' + sub.find(id='DetailPlace_uc_goldprices1_lblBLSell').text + '\n'
        + 'รับซื้อ : ' + sub.find(id='DetailPlace_uc_goldprices1_lblBLBuy').text + '\n'
        + 'ทองคำรูปพรรณ' + '\n'
        + 'ขายออก : ' + sub.find(id='DetailPlace_uc_goldprices1_lblOMSell').text + '\n'
        + 'รับซื้อ : ' + sub.find(id='DetailPlace_uc_goldprices1_lblOMBuy').text)

gold_price_check()

'''


# ===== 8/08/2020 =====
# Intro Tkinter[/]
# Tkinter create main windows [/]
# การจัดโครงสร้าง pack(), place(), grid() [*]
# Label / Entry / Button [*]

from tkinter import *
from tkinter import Tk
from tkinter import ttk
# function area

windows = Tk()
windows.title('This is my first GUI.')
windows.geometry('500x300+800+200')
#Label
lbl_hello = Label(text='Hello, Nattapong').pack(side=TOP)
lbl_tel = Label(text='Tel : 0888714699').pack(side=TOP)
lbl_email = Label(text='nattapong.ng@tot.co.th').pack(side=TOP)
lbl_username = Label(text='Username :').place(x=100, y=100)
lbl_password = Label(text='Password :').place(x=100, y=130)

# Textbox
txt_username = Entry().place(x=180, y=100)
txt_password = Entry().place(x=180, y=130)
# Button
btn_login = ttk.Button(text='LOGIN').place(x=180, y=170)
btn_clear = ttk.Button(text='CLEAR').place(x=280, y=170)

windows.mainloop()



















