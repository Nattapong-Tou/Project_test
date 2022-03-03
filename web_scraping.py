# test python for web scraping ดึงข้อมูลผู้ติดเชื้อ Covid - 19 ในไทย
from email import message
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import time, datetime
import json

# line notify covid - 19 
# line notify covid - 19  ตัวหน้าเว็บจะมี API ให้ไม่ต้องดึงจากเว็บตรงๆ โดยดึงผ่าน API รูปแบบ json 
covid_api = 'https://covid19.ddc.moph.go.th/api/Cases/today-cases-all' # api for covid-19
r_covid = requests.get(covid_api)
r_covid_data = json.loads(r_covid.content)

URL = 'https://notify-api.line.me/api/notify'
Token ='ic23VahorgzkTy3iP2xZxfuZNsXFgYeiv2XGyJ36N6v'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+Token}
print('ผู้ติด Covid-19 วันที่', r_covid_data[0]['txn_date'])

msg = (
    "\n"
    + "สรปุยอดผู้ติดเชื้อ COVID-19 ประจำวันที่ " + str(r_covid_data[0]['txn_date']) + "\n"
    + "ผู้ติดเชื้อรายใหม่ " + str(r_covid_data[0]['new_case']) + " คน" + "\n"
)
send = requests.post(URL, headers=headers, data= {'message':msg})


'''
def line_notify_message_covid(message_covid):
    payload_covid = {'message': message_covid}
    return line_notify_covid(payload_covid)

def line_notify_covid(payload_covid):
    URL = 'https://notify-api.line.me/api/notify'
    Token ='ic23VahorgzkTy3iP2xZxfuZNsXFgYeiv2XGyJ36N6v'
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+Token}     
    return requests.post(URL, headers=headers, data=payload_covid) 

def covid_check():
    

    line_notify_message_covid('จำนวนผู้ติด Covid ประจำวันที่' + str(r_covid.json()['txn_date']))
    
    
    
covid_check()
'''





# check ราคาทองแล้วส่งเข้า line notify
# ตรวจสอบราคาทองคำตัวเว็บไม่มี API เราดึงผ่านหน้าเว็บตรงๆ ไม่ต้องใช้รูปแบบ json 
web_url = 'https://www.goldtraders.or.th/default.aspx'
r = requests.get(web_url)
r.encoding = 'utf-8'
sub = BeautifulSoup(r.text)


def line_notify_message(message):
    payload = {'message':message}
    return line_notify(payload)

def line_notify(payload, file=None):
    URL = 'https://notify-api.line.me/api/notify'
    Token ='ic23VahorgzkTy3iP2xZxfuZNsXFgYeiv2XGyJ36N6v'
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+Token}     
    return requests.post(URL, headers=headers, data=payload, files=file) 

def gold_price_check():
    line_notify_message('ราคาทองคำ 96.5% ประจำวันที่ : '
        + sub.find(id='DetailPlace_uc_goldprices1_lblAsTime').text + '\n'
        + 'ทองคำแท่ง' + '\n'
        + 'ขายออก : ' + sub.find(id='DetailPlace_uc_goldprices1_lblBLSell').text + '\n'
        + 'รับซื้อ : ' + sub.find(id='DetailPlace_uc_goldprices1_lblBLBuy').text + '\n'
        + 'ทองคำรูปพรรณ' + '\n'
        + 'ขายออก : ' + sub.find(id='DetailPlace_uc_goldprices1_lblOMSell').text + '\n'
        + 'รับซื้อ : ' + sub.find(id='DetailPlace_uc_goldprices1_lblOMBuy').text)

gold_price_check()

# concept ถัดไปส่ง covid - 19 เข้า line


