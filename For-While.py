import math
import random


print('Example loop แบบ for in..')
for i in range(1, 6):
    print(i)
print('----------------------------------------------------------------')
print('เพิ่มค่าที่ล่ะสองของ step')
for i in range(2, 11, 2): #เพิ่มค่าที่ล่ะสองของ step
    print(i)
print('----------------------------------------------------------------')
print('การวน loop ย้อนกลับโดยติดลบค่าของ step')
for i in range(-10, -100, -10):
    print(i)
print('----------------------------------------------------------------')
print('การเพิ่มเงื่อนไขเข้าไปใน loop')
print('Example ต้องการตรวจสอบว่า 1-100 มีจำนวนที่ 6 และ 8 หารลงตัวกี่จำนวน')
count = 0
for i in range(1, 101):
    if (i % 6 == 0) and (i % 8 == 0):
        count += 1
print(count)

print('----------------------------------------------------------------')
print('Example รับข้อมูลจากผู้ใช้ 4 จำนวนและหาผลรวมกับค่าเฉลี่ย')
sum = 0
for i in range(1, 5):
    num = int(input(f'จำนวนที่ {i} :'))
    sum += num
print('sum : ',sum)
print('Average : ', sum /4)

print('----------------------------------------------------------------')
sum2 = 0
for i in range(1, 10):
    n = int(input(f'Number {i} :'))
    sum2 +=  n
print('Sum :',sum2)
print('----------------------------------------------------------------')

print('Example การหาค่าเลขยกกำลัง')
base = float(input('เลขฐาน : '))
power = int(input('เลขยกกำลัง (จำนวนเต็มบวก): '))
if power >= 0:
    result = 1
    for i in range(0, power):
        result *= base
        
           # เนื่องจากเลขฐานและผลลัพธ์เป็นชนิด Float ดังนั้นหากใส่หรือได้ผลลัพธ์เป็นเลขจำนวนเต็มเมื่อแสดงเลขที่มีจุดทศนิยม
           # (.0) เราอาจจะปรับเปลี่ยนการแสดงผลใหม่ได้ให้ตรงกับข้อมูลจริง
        
     #ถ้าหารด้วย  1 ลงตัวแสดงว่าเป็นจำนวนเต็ม
    if result % 1 == 0:
        result = math.trunc(result)

    if base % 1 == 0:
        base = math.trunc(base)

    print(f'{base} ** {power} = {format(result,",")}')
else:
    print('กรุณาใส่เลขยกกำลังเป็นจำนวนเต็มบวก')

print('------------------------------------------------')
print('Loop แบบ while')
print('Example 1')
x = 1
while x <= 5:
    print(x)
    x += 1
print('------------------------------------------------')
print('Example 2 แสดงการสุ่มค่าเป็นจำนวนครั้ง เพื่อให้ได้ค่ามากกว่า 0.9')
y = 0
time = 0
#สุ่มเลขที่ได้จาก  random ถ้าได้น้อยกว่า 0.9 ต้องสุ่มต่อไป
while y < 0.9:
    y = random.random()
    time += 1
print(f'จำนวนครั้งที่สุ่ม : {time}')
print('------------------------------------------------')
print('Example 3 รับค่ารหัสผ่านจากผู้ใช้แล้วตรวจสอบจนกว่าค่าจะถูกต้อง')
validcode = False
while not validcode:
    Pas = input('Input password >> ')
    if validcode == '1234':
        validcode = True

        print('Password OK.')
        break




'''
def loop1():
    for i in range(11):
        print(i)
        print("-----")
loop1()
s=0
for k in range(10): #ใส่ค่าคำสั่ง Loop ให้ระบุจำนวนที่ Input มา 10 ครั้ง
    a=float(input("Input Number :"))
    s += a #นำค่าที่ Input  เข้ามาบวกกันไปเรื่อยๆ แล้วเก็บที่ตัวแปร s
    print("Average = ",(s/10)) # นำค่ารวมทั้งหมดมาหารด้วยจำนวนที่ Input เข้าไปจะได้ค่าเฉลี่ย
    break #ออกจากการทำงานของการวน

#หาค่าเฉลี่ยจากจำนวนที่ป้อนเข้ามาเรื่อยๆ จนกว่าข้อมูลจะติดลบ
a = 0
n = 0
while True :
    t = float(input("Input Number :"))
    if t < 0 :
        print("จำนวนต้องไม่น้อยกว่า 0")
        break
    a += t
    n += 1
    if n == 0:
        print("No Data.")
    else:
        print("average =",(a/n))
        break

#แก้โจทย์คณิต
x = math.radians(float(input("Input data : ")))
n = 30
s = 0
for k in range(n+1) : # k = 0,1,......,n
    s += (-1)**k*x**(2+k+1)/math.factorial(2+k+1) # ** คือการยกกำลัง, * คือการคูณ
    print(s)
    
'''




















