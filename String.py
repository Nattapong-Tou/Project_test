import datetime
#การจัดการเกี่ยวกับอัคระ
'''
s = "Python 3.7" ; print("คำต้นฉบับ :",s)
t = s.upper(); print("upper :",t) # upper คือการทำให้ string เป็นตัวใหญ่ทั้งหมด
t = s.lower(); print("lower :",t) # lower คือการทำให้ string เป็นตัวเล็กทั้งหมด
t = s.strip(); print("strip :",t) # strip คือการทำให้ string คงเดิมทั้งหมด
t = s.capitalize(); print('Captalize :',t) # capitalize คือการทำให้ string ตัวแรกเป็นตัวใหญ่
t = s.strip().upper(); print(t) # ค่าที่ได้จะเหมือนกับ upper
k = s.find("c"); print("K = ",k) # ให้หา c ในตัวแปร s แล้วเก็บค่าไว้ใน k ผลลัพธ์คือไม่มีจะได้ค่าเป็น -1
k = "Engineering".find("ng"); print("Index =",k) # หา ng ใน Engineering

a = "hello world"
print("จำนวนตัวอักษรของ a = ",len(a)) #len() คือคำสั่งนับจำนวนอักขระในข้อความของตัวแปร a
print(a.replace("h","J")) # คำสั่ง Replace ตัวอักษรในตัวแปร a
print('-------------------------------------------------')

print('1. < โอนเงินภายในธนาคาร\t\t\t ถอนระบุจำนวนเงิน > 5')
print('2. < โอนเงินต่างธนาคาร\t\t\t สอบถามยอด > 6')
print('3. < ชำระเงินด้วยบาร์โค้ด\t\t\t เติมเงินมือถือ > 7')
print('4. < ชำระเงินและแลกเปลี่ยนสินค้า\t\t บริการอื่นๆ > 8')
print('-------------------------------------------------')
#Exercise 2-1
print('************')
print('  ********  ')
print('    ****    ')
print('     **     ')
print('      *     ')
print('-------------------------------------------------')
#Exercise 2-2
print('      1       ')
print('     222      ')
print('    33333     ')
print('   4444444    ')
print('  555555555   ')
print('-------------------------------------------------')
#Exercise 2-3
print('ผลการแข่งขันระหว่าง Man U - Liverpool')
manu = int(input('ประตูที่ Man U ทำได้ >>> '))
liverpool = int(input('ประตูที่ Liverpool ทำได้ >>> '))
print('\n')
print('ผลการแข่งขันระหว่าง asenal - chelsea')
asenal = int(input('ประตูที่ asenal  ทำได้ >>> '))
chelsea = int(input('ประตูที่ chelsea ทำได้ >>> '))
print('\n')
print('ผลการแข่งขันระหว่าง spur - mancity')
spur = int(input('ประตูที่ spur  ทำได้ >>> '))
mancity = int(input('ประตูที่ mancity ทำได้ >>> '))
print('\n')
print('สรุปผลการแข่งขัน')
print('Manunited (',manu,'-',liverpool,') Liverpool')
print('Arsenal (',asenal,'-',chelsea,') Chelsea')
print('Spur (',spur,'-',liverpool,') Man City')

print('-------------------------------------------------')



# List
x = [1,2,3]; print(x)
x = [1]*10; print(x)
x = list('a'); print(x)
'''

print('+++ String And Datetime +++')
print('+++ การจัดการแนวขอบของ string +++')
print('Python'.center(20),
      'Python'.ljust(20),
      'Python'.rjust(20),
      sep ='\n')
print('------------------------------')
print('+++ ข้อมูลชนิดวันและเวลา +++')
now = datetime.datetime.now()
print(now)
date = datetime.date.today()
print(date)
timenow = now.time()
print(timenow)
print('------------------------------')
print('+++++++ การอ่านค่าจากส่วนของวันเวลา ++++++')
dt = datetime.datetime(2019, 7, 23, 12, 22, 32)
print(dt.day)
print(dt.month)

d = datetime.date(2019,7,23)
print(d.year)
print(d.weekday()) # วันแรกของสัปดาห์

t = datetime.datetime.now()
print(t.hour)

print('------------------------------')
print('หาชื่อเต็มของวันว่าวันที่ 23-7-2019 ตรงกับวันอะไร')
print('Day')
#หาชื่อเต็มของวันว่าวันที่ 23-7-2019 ตรงกับวันอะไร
wd = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
d2 = datetime.date(2019,7,23)
w = d2.weekday()
if w == 6:
      w =0
else:
      w +=1
print('weekday : ',wd[w],'\n')

print('หาชื่อเต็มของเดือนว่าวันที่ 23-7-2019 ตรงกับวันอะไร')
print('Month')
month = ['January','February','March','April','May','June','July','August',
         'September','October','November','December']
d3 = datetime.date(2019,7,23)
month_name = month[d3.month-1]
print('Month :',month_name)

print('------------------------------')
print('Example 7-5-1 การอ่านส่วนของวันเวลาแล้วแสดงแบบ short,Medium,Long')
thai_day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
thai_month = ['January','February','March','April','May','June','July','August',
         'September','October','November','December']

dt2 = datetime.datetime.now()
wd2 = 0 if dt2.weekday() == 6 else dt2.weekday() + 1
day = dt2.day
month2 = dt2.month
year = dt2.year + 543
hour = dt2.hour
minute = dt2.minute
secon = dt2.second
print(f'วันเวลาแบบสั้น :{day}/{month2}/{year}')
print(f'วันเวลาแบบปกติ :{day} {thai_month[month2-1]} {year}')



