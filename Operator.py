import math
import random #module ใช้สำหรับสุ่มตัวเลข
#Exmample 1

quantity = int(input('จำนวนสินค้าที่ซื้อ : '))
price = float(input('ราคาสินค้า : '))
total = price*quantity
print('รวมเป็นเงิน :',total)
pay = float(input('จำนวนเงินที่จ่าย : '))
chang = pay-total
print('เงินทอน :',chang)
print('-------------------------------------------------')
#Exmample 2
a=10
b=20
print(f'ก่อนสลับค่า a={a},b={b}')
b=a+b
a=b-a
b=b-a
print(f'หลังสลับค่า a={a},b={b}\n')
a=108
b=-1009
print(f'ก่อนสลับค่า a={a},b={b}')
b=a+b
a=b-a
b=b-a
print(f'หลังสลับค่า a={a},b={b}\n')
print('-------------------------------------------------')
#Exmample 3 หาจำนวนธนบัตรของ ATM
withdraw = int(input("จำนวนเงินที่จะถอน ="))
b1000 = withdraw // 1000 # // คือการหารแบบเอาจำนวนเต็ม
remain = withdraw % 1000 #หาค่าที่เหลือจากการหารด้วย 1000
b500 = withdraw // 500
remain = withdraw % 500
b100 = withdraw // 100
print(f'ธนบัตรที่ได้ \nb1000={b1000}\nb500 = {b500}\nb100 = {b100}')
print('-------------------------------------------------')

# Operator สำหรับการคำนวนและการกำหนดค่า
x = 5
x += 1 #บวกค่าเดิมเพิ่มไปอีก 1
print(x)
y = 5
y -= 1 #ลบค่าเดิมเพิ่มไปอีก 1
print(y)
s = 'Python Programming '
s += 'For Beginner'
print(s)
print('-------------------------------------------------')
#Example 4 รับตัวเลข 5 จำนวนแล้วหาค่าเฉลี่ย
sum = 0
sum += float(input('Number 1 ='))
sum += float(input('Number 2 ='))
sum += float(input('Number 3 ='))
sum += float(input('Number 4 ='))
sum += float(input('Number 5 ='))
average = sum / 5
print('\nTatal = ',sum)
print('Average = ',average)
print('-------------------------------------------------')
#Example 5 การหาหลักของตัวเลข
n = int(input('Please input number 5 state :'))
x = n
x //= 10000
print('หลักหมื่น =',x)
x = n
x %= 10000
x //= 1000
print('หลักพัน =',x)
x = n
x %= 1000
x //= 100
print('หลักร้อย =',x)
x = n
x %= 100
x //= 10
print('หลักสิบ=',x)
x = n
x %= 10
print('หลักหน่วย =',x)
print('-------------------------------------------------')

#function for number
maxnumber = max(1000,234,3000,23)
print('Maxnumber =',maxnumber)
minnumber = min(10,3,4,2,1000)
print('Minnumber = ',minnumber)
#เลขยกกำลัง
m = pow(2,2)
print('สอลยกกำลังสอง =',m)
#การสร้างเลขสุ่ม
a = random.randint(1,10)
print('ค่า Random ของ a =',a)
b = random.random()
print('ค่า Random ของ b =',b) # Random ที่ไม่ได้กำหนดจำนวนให้
print('-------------------------------------------------')
#Example การสุ่มตัวเลขรางวัลของ Lotto
print('รางวัลเลขท้ายสองตัว : ',end='')
number2 = f'{random.randint(0,9)}{random.randint(0,9)}'
print(number2)
print('รางวัลเลขหน้าสามตัว : ',end='')
FNumber = f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
FNumber2 =f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
print(FNumber,FNumber2)
print('รางวัลเลขท้ายสามตัว : ',end='')
RNumber= f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
Rnumber2= f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
print(RNumber,Rnumber2)
print('-------------------------------------------------')

#exercise 3-1 หาพื้นที่รูปหลายเหลี่ยม
print('exercise 3-1 หาพื้นที่รูปหลายเหลี่ยม')
n = float(input('จำนวนด้าน : '))
s = float(input('ความยาวของแต่ล่ะด้าน : '))
polygon_area = (n+s**2)/4*(math.tan((math.pi/n)))
print('รูปหลายเหลี่ยมมีด้าน ',n,' ด้าน ความยาวด้านละ ',s,' จะมีพื้นที่ Area = ',polygon_area)
print('-------------------------------------------------')
#exercise 3-2 คำนวนหามูลค่าการลงทุนในอนาคต
print('exercise 3-2 คำนวนหามูลค่าการลงทุนในอนาคต')
amount = float(input('จำนวนเงินลงทุนเริ่มแรก >> '))
r = float(input('อัตราดอกเบี้ย (%) >> '))
period = int(input('จำนวนปีที่ลงทุน >> '))
rate = (r/100) #เทียบดอกเบี้ยเป็นเปอร์เซ็นต์
fv = amount*(1+rate)**period
print('มูลค่าของเงินที่ลงทุนในอนาคตคือ >> ',(format(fv, ',.2f'))) #จัด Format แบบคั่นหลักพันและแสดงทศนิยมสองตำแหน่ง
print('-------------------------------------------------')

#exercise 3-3 สุ่ม Password
print('exercise 3-3 สุ่ม Password')
print('Your password is : ', end='')
randomp = f'{random.choice("abcdefghijklmnopqrstuvwxyz")}{random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}' \
          f'{random.randint(0,9)}{random.randint(0,9)}' \
          f'{random.choice("abcdefghijklmnopqrstuvwxyz")}{random.choice("abcdefghijklmnopqrstuvwxyz")}'
print(randomp)
print('-------------------------------------------------')
#exercise 3-4 สุ่มตัวเลขแล้วนำมาหาชั่วโมงนาทีวินาที
print('exercise 3-4 สุ่มตัวเลขแล้วนำมาหาชั่วโมงนาทีวินาที')
randomnumber = int(f'{random.randint(100000,1000000)}')
#print(randomnumber)
save = randomnumber
save //= 3600
save2 = randomnumber
save2 %= 3600
save2 //= 60
save3 = randomnumber
save3 %= 60
save3 //= 1
print('เวลาเท่ากับ',save,' ชั่วโมง ',save2,'นาที ',save3,' วินาที')
print('-------------------------------------------------')
#exercise 3-4 หาค่าจำนวนเงินที่จ่ายไปว่าจ่ายจำนวนเท่าไหร่
print('exercise 3-4 หาค่าจำนวนเงินที่จ่ายไปว่าจ่ายจำนวนเท่าไหร่')
money = float(input('ใส่จำนวนเงิน >> '))
money2 = money
money2 //= 1000
print('แบงค์ 1000 =',(format(money2,',.0f'))) #จัด format แบบไม่เอาทศนิยม
money2 = money
money2 %=1000
money2 //= 100
print('แบงค์ 100 =',(format(money2,',.0f'))) #จัด format แบบไม่เอาทศนิยม
money2 = money
money2 %= 100
money2 //= 50
print('แบงค์ 50 =',(format(money2,',.0f'))) #จัด format แบบไม่เอาทศนิยม
money2 = money
money2 %= 50
money2 //= 20
print('แบงค์ 20 =',(format(money2,',.0f'))) #จัด format แบบไม่เอาทศนิยม
money2 = money
money2 %= 20
money2 //= 10
print('เหรียญ 10 =',(format(money2,',.0f'))) #จัด format แบบไม่เอาทศนิยม
money2 = money
money2 %= 10
money2 //= 5
print('เหรียญ 5 =',(format(money2,',.0f'))) #จัด format แบบไม่เอาทศนิยม
money2 = money
money2 %= 5
money2 //= 1
print('เหรียญ 1 =',(format(money2,',.0f'))) #จัด format แบบไม่เอาทศนิยม
money2 = money
money2 %= 1
money2 //= 0.50
print('เหรียญ 50 สตางค์ =',(format(money2,',.0f'))) #จัด format แบบไม่เอาทศนิยม
money2 = money
money2 %= 0.50
money2 //= 0.25
print('เหรียญ 25 สตางค์ =',(format(money2,',.0f'))) #จัด format แบบไม่เอาทศนิยม
print('-------------------------------------------------')











