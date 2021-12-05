import math # import class math เพื่อนำ function class ที่ใช้ในการคำนวนมาใช้งาน


# ทดสอบการใช้ If - Else ในโปรแกรมคำนวน Lotto
'''
p1,p2,p3,n1,n2 = [int(e) for e in input("Input Lotto :").split()] #รับข้อมูลใส่ตัวแปร .split คือตัดช่องว่าง
 su = 0 #ตัวแปรนี้ใช้เก็บเงินรางวัลรวม
 if n1 <= p1 <= n2 :
   su+= 10000
 if n1%100 <= p2 :
   su += 25
 
su += 25*(n2//100 - n1//100 - 1)
if n1%1000 <= p3 :
   su+=100
if p3 <= n2%1000 :
    su+=100

su += 100*(n2//1000 - n1//1000 - 1)
print(su)

'''
#โปรแกรมตัดเกรด
score = float(input("Input Score :"))
if 80 <= score <= 100 :
    print("Grade A !!")
elif 75 <= score <= 80 :
    print("Grade B+ !!")
elif 70 <= score <= 75 :
    print("Grade B !!")
elif 65 <= score <= 70 :
    print("Grade C+ !!")
elif 60 <= score <= 65 :
    print("Grade C !!")
elif 55 <= score <= 60 :
    print("Grade D+ !!")
elif 50 <= score <= 55 :
    print("Grade D !!")
elif 0 <= score <= 50 :
    print("Grade F !!")

else:
    print("Error !!")
print('-------------------------------------------------')
#การหาค่าดัชนีมวลกาย

wight = float(input("Input your wight : "))
#ตรวจสอบค่าที่รับเข้ามา
if wight < 10 :
    print("Data is not possible !")
    exit(wight)
if wight > 500 :
    print("Data is not possible !")
    exit(wight)

height = float(input("Input your height : "))
if height < 10 :
    print("Data is not possible !")
    exit(height)
if height > 500 :
    print("Data is not possible !")
    exit(height)

hm = height/100
if hm == 0 :
    print("Data is not calculate.")
    exit(hm)
else :
    bmi = wight/hm**2
    print("Your BMI is :",bmi)

if 0 < bmi <= 18.50 :
    print("น้ำหนักน้อย/ผอม")
elif 18.50 < bmi <= 22.90 :
    print("ปกติ/สุขภาพดี")
elif 22.90 < bmi <= 24.90 :
    print("ท้วม/โรคอ้วนระดับ 1")
elif 24.90 < bmi <= 29.90 :
    print("อ้วน/โรคอ้วนระดับ 2")
else:
    print("อ้วนมากกก")

print('-------------------------------------------------')

print('Operator ในการเปลียบเทียบค่าของตัวแปร')
a = (1 == 2)
b = (5 == 5)
c = (a == b)

# ต่าที่ส่งออกมาจะเป็น True or false เท่านั้น เช่น 1 == 2 ค่าที่ได้จะเป็น False เนื่องจากเงื่อนไขเป็นเท็จ
# ใน  Python True = 1, False = 0



print('\n 1 == 2 :',a,'\n 5 == 5 : ',b,'\n a == b : ',c)
d = (10 <= 20)
e = (10 >= 20)
print('\n 10 <= 20 =',d,'\n 10 >= 20 =',e)
print('-------------------------------------------------')
if True:
    print('Hello World') # บรรทัดนี้จะถูกประมวลผลเนื่องจากเป็นจริง
if False :
    print('End') # บรรทัดนี้ไม่ถูกประมวลผลเนื่องจากเงื่อนไงเป็นเท็จ

a = False
if a :
    print('a = False')
    print('Operator a is False..')
# Block จะไม่ถูกประมวลผลเนื่องจากค่าเป็นเท็จ
# ถ้าในบล๊อกมี 1 คำสั่งสามารถพิมพ์ต่อไปได้เลย
if True : print('ในบล๊อกมี 1 คำสั่งสามารถพิมพ์ต่อไปได้เลย')
if False : print('ในบล๊อกมี 1 คำสั่งสามารถพิมพ์ต่อไปได้เลย')
print('-------------------------------------------------')
print('If Else with Comparison Operator')
f = 10
g = 20
print('ค่าตัวแปร f :',f,'ค่าตัวแปร g:',g)
if f <= g :
    print('ตัวแปร F มีค่าน้อยกว่าหรือเท่ากับ g')

balance = int(10000)
withdraw = int(30000)
print('ยอดเงินคงเหลือ :',balance)
if withdraw > 20000 :
    print('จำนวนเงินที่ถอนต้องไม่เกิน 20000')
if withdraw > balance :
    print('จำนวนเงินที่ถอดต้องไม่มากกว่ายอดเงินคงเหลือ')
print('-------------------------------------------------')
print('ตัวอย่างตรวจสอบเงื่อนไขหารตัวเลข')
h = int(input('h ='))
i = int(input('i ='))
if i == 0:
    print('ตัวหารเป็น 0 ไม่ได้ครับ')
if i != 0:
    j = h/i
    j = format(j,'.2f')
    print(f'{h} / {i} = {j}')

print('-------------------------------------------------')
print('Example 4-3-1 รับตัวเลขเข้ามาแล้วตรวจสอบว่าเป็นเลขคู่หรือเลขคี่')
odd = 'เลขคี่'
even = 'เลขคู่'
k = int(input('จำนวนที่ 1 : '))
l = odd
if k % 2 == 0:
    l = even
print(f'{k} as {l}')
m = int(input('จำนวนที่ 2 : '))
l = odd
if m % 2 == 0 :
    l = even
print(f'{m} as {l}')

print('-------------------------------------------------')
print('Example 4-3-2 หาตัวเลขมากที่สุดจาก 3 จำนวน')
n1 = int(input('Number 1 : '))
max = n1
n2 = int(input('Nunber 2 : '))
if n2 > max :
    max = n2
n3 = int(input('Nunber 3 : '))
if n3 >  max:
    max = n3
print('\nจำนวนที่มากที่สุดคือ ',max)

print('-------------------------------------------------')
print('การใช้คำสั่ง if - else')
n = 99
remain = n % 2
if remain == 0:
    print(n,'เป็นเลขคู่')
else:
    print(n, 'เป็นเลขคี่')

number1 = int(input('Number 1 = '))
number2 = int(input('Number 2 = '))
if number2 == 0 :
    print('ตัวหารเป็น 0 ไม่ได้')
else:
    number3 = number1 / number2
    print(f'{number1}/{number2} = {number3}')

isLeapYear = False
NumDayInYear = 0
if isLeapYear:
    NumDayInYear = 366
else:
    NumDayInYear = 365

p = -1
if p >= 0:
    print('OK')
else:
    pass # pass คือข้ามบล๊อกนี้ไปก่อนโดยไม่ต้องนำมาประมวลผล
print('-------------------------------------------------')

print('Example 4-4-1 รับข้อมูล Password and confirm password')
password1 = input('Password : ')
password2 = input('Confirm Password : ')
if password1 != password2 :
    print('Password not match !')
else:
    print('Password OK') 
print('-------------------------------------------------')



print('-------------------------------------------------')
print('IF ซ้อน IF')
login = input('Username >> ')
password3 = input('Password >> ')
if login == 'admin':
    print('Username or Password was wrong')

    if password3 == '1234':
        print('Login Success.')
else:
    print('Username or Password was wrong')

print('-------------------------------------------------')
print('Example Test Check Relationship')

gender = input('Gender (Male,Female) : ')
age = int(input('Age : '))
relation = int(input('0 = Single,1 = Married : '))
if gender != 'Male' or 'male':
    print('Data can not insert.')
if age > 150 :
    print('Data can not insert.')
if age < 0 :
    print('Data can not insert.')
if gender == 'Female' :
    if age < 30 :
        if relation == 0:
            print('คุณคือคนที่เรากำลังตามหา')
else:
    print('ขอพิจารณาใหม่นะครับ')

print('-------------------------------------------------')
print('Example ทดสอบเปรียบเทียบ Generation.')
year = int(input('พ.ศ. เกิด : '))
generation = ''
if year <= 2443 :
    generation = 'Lost generation'
elif (year >= 2444) and (year <= 2467):
    generation = 'Greatest generation'
elif (year >= 2468) and (year <= 2488):
    generation = 'Silent generation'
elif (year >= 2489) and (year <= 2507):
    generation = 'Baby Boomer generation'
elif (year >= 2508) and (year <= 2519):
    generation = 'generation Y'
elif (year >= 2520) and (year <= 2538):
    generation = 'generation X'
elif year > 2539 :
    generation ='generation Z'
else:
    print('Data is not complese.')
print(f'ปี พ.ศ. เกิด : {year} จัดอยู่ในกลุ่ม {generation}')

























