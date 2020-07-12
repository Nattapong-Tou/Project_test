import math
import random
"""
    คอมเม้นแบบหลายๆ บรรทัด
    
"""
print('+++ Function แบบไม่ส่งค่ากลับ +++')
def print_hello(): # Function แบบไม่มีค่าพารามิเตอร์
    print('Hello')

def print_text(text): # Function แบบมีค่าพารามิเตอร์
    print(text)

print_hello() # Call Function
print_text('Hi Nattapong') # เรียกใช้ Function แล้วส่งค่าพารามิเตอร์ให้
print_text('Hi Niracha') # เรียกใช้ Function แล้วส่งค่าพารามิเตอร์ให้

print('-------------------------------------------------')
print('+++ Function แบบส่งค่ากลับ +++')
'''
def select_menu():
    print('กรุณาเลือกเมนู')
    # menu = input('1 = ถอน 2 = ถามยอด 3 = โอน 0 = ยกเลิก >>')
    # return  menu
select_menu()
'''
def random_A_to_Z():
    A = ord('A')
    Z = ord('Z')
    r = random.randint(A,Z)
    return chr(r)
result = random_A_to_Z() # นำค่าที่ได้มาใส่ในตัวแปร
code = random_A_to_Z() + random_A_to_Z() + random_A_to_Z()
print(random_A_to_Z()) # ค่าที่ได้จะได้ตัวเดียว
print(code) # ค่าที่ได้จะได้สามตัว

if random_A_to_Z() == 'E':
    print('Error')

print('-------------------------------------------------')
print('Function แบบส่งค่ากลับมากกว่า 1 ค่า')
def random_3_digits():
    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,9)
    d = [a,b,c]
    return d

data = random_3_digits()
print(data)

for x in random_3_digits():
    print(x)

print('-------------------------------------------------')
print('การหยุดการทำงานของ Function')
def circle_area(radius):
    if radius <= 0:
        return
    else:
        return 3.14 * radius ** 2
r_0 = circle_area(0)
print(r_0)
r_10 = circle_area(10)
print('Radius = 10 area :',r_10)

if circle_area(0.0) == None:
    print('Error')

print('-------------------------------------------------')
print('Example 8-3-1 สุ่มตัวเลข lotto')
def rand_num(length):
    result2 =''
    for n in range (0, length):
        r = random.randrange(0,9)
        result2 += str(r)
    return result2
print(
    'รางวัลที่ 1 :',rand_num(6),'\n',
    'รางวัลเลขหน้า 3 ตัว :',rand_num(3),' ',rand_num(3),'\n',
    'รางวัลเลขท้าย 3 ตัว :', rand_num(3), ' ', rand_num(3), '\n',
    'รางวัลเลขท้าย 2 ตัว :', rand_num(2)
)

print('-------------------------------------------------')
print('Example 8-6-1 การจัดเก็บข้อมูลส่วนกลางด้วยตัวแปรแบบ Global')
balance = random.randint(10000, 50000)
menu = 1
amount = 0
def select_menu():
    global menu
    print('\nPress select menu.')
    menu = input('1 = ถอน 2 = ถามยอด 3 = โอน 0 = ยกเลิก >>')
    if not menu.isdigit() or int(menu) not in range(1, 4):
        exit(0)
    else:
        menu = int(menu)

    if menu in range(1,3):
        get_amount()
    elif menu == 3:
        show_balance()

def get_amount():
    global amount
    a = input('Amount >> ')
    if not a.isdigit():
        print('Amount is not int.')
        get_amount()
    else:
        amount = int(a)
        if menu == 1:
            deposit()
        elif menu == 2:
            withdraw()
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
        print('Your amount is not avvarable.')

def show_balance():
    print('Amount :',format(balance,','))
    select_menu()

show_balance()
select_menu()
'''
def random_boolean():
    a = random.randint(0,1)
    b = False if a == 0 else True
    print_text2(b)
def print_text2(text2):
    print_text2(text2)

random_boolean()


def MyFirstFunction ():
    print("This my first function.")
MyFirstFunction() #เรียก Function มาใช้งาน

def MyFunction (fName):
    print(fName + " Refsnes")
# ส่งค่าเข้าไปใน Function เพื่อนำไปประมาลผล
MyFunction("Email")
MyFunction("Name")
MyFunction("Telephone")

def MyFunction2 (country ="Thailand"):
    print("I'm from ",country)
MyFunction2() #เรียก Function มาทำงานโดยจะแสดงค่า Defult เป็น Thailand เพราะเราไม่ได้ส่งค่าเข้าไป
MyFunction2("India") # เมื่อเราส่งค่าเข้าไป Function จะไม่แสดงค่า Defult แต่จะแสดงค่าที่ส่งเข้าไป
MyFunction2("Japan")

def MyFunction3(food):
    for x in food:
        print(x)
Fruits = ["apple","mango","rambuten","grap"]
cloth = ["Levi's","Mac","Arrow"]
MyFunction3(Fruits)
MyFunction3(cloth)

class person:
    def __init__(self, name, age) : # ถ้าเป็น __init__ จะเรียกใช้ออโต้เลย
        self.name = name
        self.age = age

    def myfunc(self):
        print("My name is :", self.name)
        print("My age :",self.age)

p1 = person("Nattapong","27")
print("Your are :",p1.name,",And age :",p1.age)
p1.myfunc() #นำค่า p1 ใส่ใน myfunc แล้วนำมาแสดงผล

def rectangle(w,h):
    area = w*h
    return area
def triangle(w,h):
    return .5*w*h


w = float(input("input w :"))
h = float(input("Input h :"))
print("พื้นที่รูปสี่เหลี่ยมคือ =",rectangle(w,h))
print("พื้นที่รูปสามเหลี่ยมคือ =",triangle(w,h))

# เขียนโปรแกรมคำนวนเลขโทรศัพท์มงคล
def sum_phone_diff(phone_number):
    total=0
    for c in phone_number: #0888888888
        total =+ int(c)
        return total

print(sum_phone_diff("0888714699"))

'''












