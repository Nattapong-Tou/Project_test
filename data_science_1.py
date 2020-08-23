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










