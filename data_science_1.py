# rang (strat, stop, step)
'''
a = range(0, 10, 2)

for x in a:
    print(x)

# ตรวจสอบค่า start, stop, step
print('------ ตรวจสอบค่า start, stop, step -------')
start = a.start
stop = a.stop
step = a.step
print('Start = ', start)
print('Stop = ', stop)
print('Step = ', step)
'''

# รายการข้อมูลแบบ list
'''
# สร้าง list โดยใช้ function
a = list() # list ว่างเปล่า
b = list([1, 2, 3, 4, 5]) # list ที่มีสมาชิก 1, 2, 3, 4, 5
c = list(['one', 'two', 'tree']) # list แบบ string
d = list(range(1, 5)) # สร้าง list โดยใช้ rang()

# สร้าง list โดยใช้ []
e = [1, 2, 3, 4, 5]
f = ['one', 'two', 'tree']
g = [range(1, 5)]
'''

# functoin built in ที่สามารถใช้งานร่วมกับ list 
'''
e = [1, 2, 3, 4, 5]
print('จำนวนสมาชิกทั้งหมดใน list = ', len(e)) # len = จำนวนสมาชิกทั้งหมดใน list
print('ผลรวมทั้งหมดใน list = ', sum(e)) # ผลรวมทั้งหมดใน list
print('ค่ามากสุดใน list = ', max(e)) # ค่ามากสุดใน list
print('ค่าน้อยสุดใน list = ', min(e))
'''
# 29 / 08 / 2020
import pandas as pd

#การกำหนดข้อมูลให้กับ Series
data1 = [70, 85, 50, 75] # >> list
sr1 = pd.Series(data=data1)

data2 = (10, 20, 30, 40) # >> tuple
sr2 = pd.Series(data2)

sr3 = pd.Series([20, 40, 60, 80])

print(sr1)

# กำหนด index ลงไปด้วย
index = ['A', 'B', 'C', 'D']
sr4 = pd.Series(data1, index=index)
print(sr4)

# values and index
data3 = {'T-Shirt': 499, 'shoe': 2000, 'Bag': 40000}
sr5 = pd.Series(data3)
print(sr5.index, sr5.values, sep='\n\n')





