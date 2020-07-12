import math #import class math เพื่อนำ function class ที่ใช้ในการคำนวนมาใช้งาน

#ทดสอบการแสดงค่าเข้าเพื่อประมวลผล
x = input ("Press enter ... : ")
y = input ("Press enter ... : ")
print("Key",x+y)

a = 5
b = 5
print(a+b)


#แบบฝึกหัด
#ลองสร้างตัวแปร h,m,s เพื่อเก็บข้อมูลชั่วโมง,นาที,วินาที แล้วนำทั้งหมดมาปสดงเป็นวินาที
h = int(input("Input Hour :"))
m = int(input("Input Minuse :"))
s = int(input("Input Second :"))
print("Resule :",((a*6)*60)+(m*60)+s,"Seconds")

#โปรแกรมคำนวนแบบเลข log
# x = float(input("Input Data : "))
# y = 2-x+(3/7)*xe2-(5/11)*xe3+(math.log(x))

#โปรแกรมคำนวนพื้นที่สามเหลี่ยม
a = float(input("Input Data a :"))
b = float(input("Input data b :"))
c = float(input("Input data c :"))
cr = c*math.pi/180 # เรียก Function Math ของค่า ไพอาร์ มาคำนวนก่อน
area = 1/2*a*b*math.sin(cr)
print("Area = ",area,"SQ CM")

#ทดสอบแปลงอุณหภูมิ
celcies = float(input("Input Celcise :"))
Fahrenheit = (9/5)*celcies+32
Kelvin = celcies+273.15
print("Fahrenheit =",Fahrenheit,"F")
print("Kelvin = ",Kelvin,"K")

#ทดสอบหาพื้นที่รูปสามเหลี่ยมแบบที่ 2

a = float(input("Input a :"))
b = float(input("Input b :"))
c = float(input("Input c :"))
x = (a*a)+(b*b)-2*(a*b)*math.cos(c)
print("Area =",x)







