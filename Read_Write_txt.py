import datetime
import os

'''
print('การอ่านไฟล์ txt')
try:

    file = open('file/TestRead.txt',mode='r+',encoding='UTF-8') # เปิดไฟล์ตาม location
    print(file.read())
    file.seek(0)


except Exception as err :
    print(err)

else:
    file.close()


print('---------------------------')
print('การเขียนไฟล์ txt')
try:
    file2 = open('file/TestWrite.txt', mode='a+', encoding='UTF-8')
    # file3 = open('file/TestWrite.txt', mode='a+', encoding='UTF-8')
    print('รายชื่อพนักงาน',file = file2)
    print('Wuttichai',file=file2)
    print('Nattapong',file=file2)
    print('Niracha',file=file2)
    print('Tou',file=file2)

except IOError as err2:
    print(err2)
else:
    file2.close()

print('====================================')
print('การกระทำกับไฟล์และ directory')
print('ทดสอบเปลี่ยนชื่อไฟล์')

try:
    if os.path.exists('file/TestRead.txt') :
        os.rename('file/TestRead.txt','file/TestRead2.txt') # Rename file
        # os.makedirs('file/TestCreat.txt') # Test Create or directory file .txt


    else:
        os.makedirs('file/TestRead.txt') # Create File if file is not

except IOError as err:
    print(err)

'''
print('====================================')
print('Example 10-4-1 ทดสอบการสร้าง log file')

print('*** ถ้าต้องการยกเลิก กด Enter โดยไม่ต้องใส่ข้อมูล')
try:
    with open('file/TestLogFile.txt', mode='a+', encoding='UTF-8') as logfile:
        while True:
            data = input('Even now >> ')
            if data == '':
                break

            # ตัดเวลา microsec ออก
            dt = datetime.datetime.now().replace(microsecond=0)
            # นำวันเวลาและข้อมูลมาเขียนลงในไฟล์
            logfile.write(str(dt) + ' -- ' + data + '\n')

except IOError as err:
    print(err)













