

# hello world
# hello Nattapong

'''
import keyword
print(keyword.kwlist)
hello world
hello Nattapong

# ประกาศตัวแปรพร้อมกำหนดค่าไปด้วย จะประกาศตัวแปรแล้วไปกำหนดค่าภายหลังไม่ได้
x = hello       #OK
y = Nattapong   #OK
a = x           #OK
b = x + y       #OK

# ตัวแปรที่กำหนดค่าไว้ตั้งแต่ต้นแล้วสามารถเปลี่ยนค่าในภายหลังได้
number = 1
number = 2
number = 3

x = 100
y = 234.45
a = -10
b = -10.5

x = 100.4 #เดิม X เป็นจำนวนเต็ม

print('hello')
print("สวัสดี")
print('123')
print() # บรรทัดว่าง

languase = 'Python'
Version = '3.8'
print(languase)
print(Version)

name = str(input('Enter your name :'))
age = str(input('Enter your age :'))
tall = str(input('Enter your height :'))
print(f'your info => name :{name}, age :{age} years old, tall :{tall} cm')

price = input('ราคา :')
price = float(price)
quantity = int(input('จำนวนที่ซื้อ :'))
total = price*quantity
print(f'ราคาทั้งหมด : {total}')
x = 10 + 10
print(x)
y = 10/2
print(y)
a = 2 * 2
print(a)
b = 10.5 + 10.2
print(b)


# Example if - else
x = 90 
remain = x % 2 
if remain == 0: # ถ้า x หารด้วย 2 ลงตัวแสดงว่าเป็นเลขคู่
    print(x, 'เป็นเลขคู่')
else:
    print(x, 'เป็นเลขคี่') 


print('Select your level.')
level = input(str('Enter your level(1 - 4) : '))
if level == '1':
    print('Easy level')
elif level == '2':
    print('Medium level')
elif level == '3':
    print('Hard level')
elif level == '4':
    print('Expert level')
else:
    print('Level not active.')


for i in range(1,6):
    print(i)
sum = 0
for i in range(1,5):
    num = int(input(f'จำนวนที่ {i} : '))
    sum += num

print('ผลรวม :', sum)
print('ค่าเฉลี่ย :', sum / 4)

x = 1
while x <= 5:
    print(x)
    x += 1


import random # import library ของ python มาใช้ในการ random ตัวเลข
x = 0
time = 0
# เลขสุ่มที่ได้จาก random() จะอยู่ระหว่าง 0 - 1 ถ้าค่าที่ได้น้อยกว่า 0.9 ให้วน loop ต่อไป
while x < 0.9:
    x = random.random()
    time += 1 # เก็บค่าจำนวนครั้ง

print(f'ต้องสุ่มทั้งหมด {time} ครั้ง เพื่อให้ได้เลขตั้งแต่ 0.9 ขึ้นไป')
'''
validcode = False
while not validcode : # ถ้าตัวแปร validcode เป็น false ให้วน loop ต่อไป
    code = input('Input your password >> ')
    if code != '1234' :
        print('Bad password please try again.')
    if code == '1234':
        validcode = True
        print('Thank you for login.')









