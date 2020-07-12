import random


print('Test Try Beginner.')
'''
try:
    x = input('กรุณาใส่เลขจำนวนเต็ม : ')
    y = int(x)
except:
    print('Error ข้อมูลที่ใส่ไม่ใช่จำนวนเต็ม')

else:
    print('y = ',y)
print('good bye.')
print('====================================')
print('Example 9-2-1 วาง try ไว้ใน while จนกว่าค่าจะถูกต้อง')
while True:
    try:
        a = int(input('กรุณาใส่เลขจำนวนเต็ม : '))
        break
    except:
        print('ท่านใส่ข้อมูลไม่ถูกต้อง')
        continue
print('Thank you')
print('====================================')
'''
print('Example 9-2-2 สร้าง Function Recursion')
def get_int():
    try:
        b = int(input('กรุณาใส่เลขจำนวนเต็ม >> '))
        return b
    except:
        print('ท่านใส่ข้อมูลไม่ถูกต้อง')
        get_int() # ถ้าเกิดข้อผิดพลาดจะเรียกตัวมันเองขึ้นมาทำงาน
b = get_int()
print('Thank.')
print('====================================')
print('try except finally')
text_num = ['zero','one','two','three','four','five']
r = random.randint(0,10)
try:
    text = text_num[r]
except:
    print('Index out of rang')
else:
    print('Text = ',text)
finally:
    print('random num = ',r)

print('====================================')
print('การระบุชนนิดข้อผิดพลาด')
print('การตรวจสอบข้อผิดพลาดชนิดเดียว')
try:
    y = random.randint(0,1)
    x = 1 / y
except ZeroDivisionError as arr :
    print(arr)


















