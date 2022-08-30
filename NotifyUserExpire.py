# script ตรวจสอบ User ที่กำลังจะสิ้นสุดอายุลงของ Monitor SolarWidns 
import sqlite3
import requests

# connectDB
con = sqlite3.connect('Database/db.sqlite3')
con.cursor()
#print('connected')

sql = "SELECT * FROM myweb_solarwinds_username_data WHERE julianday(date_out) - julianday(date()) <= 30.0" # SQL ตรวจสอบ Username ที่กำลังจะสิ้นสุดอายุลงในอีก 30 วัน
rows = con.execute(sql)

for i in rows :
    if i != " " :
        # Notify with line
        URL = 'https://notify-api.line.me/api/notify'
        Token ='ic23VahorgzkTy3iP2xZxfuZNsXFgYeiv2XGyJ36N6v'
        headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+Token}
        message = "แจ้งเตือน Username ที่ขอใช้งานระบบ Service Monitor SolarWinds ใกล้จะสิ้นสุดอายุการใช้งาน กรุณาตรวจสอบ."
        r = requests.post(URL, headers=headers, data={'message' : message})
        break 
    else:
        break

'''
Powershell script notify when user log on to VM Server
$url = 'https://notify-api.line.me/api/notify'
$token = 'Bearer ic23VahorgzkTy3iP2xZxfuZNsXFgYeiv2XGyJ36N6v'
$header = @{Authorization = $token}
$body = @{message = 'Alert : Someone have a remote to this VM Server as ' + $env:USERNAME + ' User On ' +$env:COMPUTERNAME+ ' Server'}
$res = Invoke-RestMethod -Uri $url -Method Post -Headers $header -Body $body
echo $res 

'''





 





















