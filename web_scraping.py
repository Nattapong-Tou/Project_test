# test python for web scraping ดึงข้อมูลผู้ติดเชื้อ Covid - 19 ในไทย

import requests
from bs4 import BeautifulSoup
import pandas as pd 
import time


# line notify covid - 19 
# line notify covid - 19  ตัวหน้าเว็บจะมี API ให้ไม่ต้องดึงจากเว็บตรงๆ โดยดึงผ่าน API รูปแบบ json 
covid_api = 'https://covid19.th-stat.com/api/open/today' # api for covid-19
r_covid = requests.get(covid_api)
r_covid.encoding = 'utf-8'

def line_notify_message_covid(message_covid):
    payload_covid = {'message': message_covid}
    return line_notify_covid(payload_covid)

def line_notify_covid(payload_covid):
    URL = 'https://notify-api.line.me/api/notify'
    Token ='ic23VahorgzkTy3iP2xZxfuZNsXFgYeiv2XGyJ36N6v'
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+Token}     
    return requests.post(URL, headers=headers, data=payload_covid) 

def covid_check():
    
    line_notify_message_covid('จำนวนผู้ติด Covid ประจำวันที่ '
        + str(r_covid.json()['UpdateDate']) + '\n'
        + 'ผู้ป่วยสะสม : ' + str(r_covid.json()['Confirmed'])  + '\n'
        + 'ผู้ป่วยหายแล้ว : ' + str(r_covid.json()['Recovered']) + '\n'
        + 'ผู้ป่วยที่อยู่ รพ. : ' + str(r_covid.json()['Hospitalized']) + '\n'
        + 'ผู้ป่วยใหม่ : ' + str(r_covid.json()['NewConfirmed'])+ '\n'
        + 'เสียชีวิต : ' + str(r_covid.json()['Deaths']))
    
covid_check()


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
    line_notify_message('ราคาทองคำ 96.5% ประจำวันที่'
        + sub.find(id='DetailPlace_uc_goldprices1_lblAsTime').text + '\n'
        + 'ทองคำแท่ง' + '\n'
        + 'ขายออก : ' + sub.find(id='DetailPlace_uc_goldprices1_lblBLSell').text + '\n'
        + 'รับซื้อ : ' + sub.find(id='DetailPlace_uc_goldprices1_lblBLBuy').text + '\n'
        + 'ทองคำรูปพรรณ' + '\n'
        + 'ขายออก : ' + sub.find(id='DetailPlace_uc_goldprices1_lblOMSell').text + '\n'
        + 'รับซื้อ : ' + sub.find(id='DetailPlace_uc_goldprices1_lblOMBuy').text)

gold_price_check()

# concept ถัดไปส่ง covid - 19 เข้า line


'''
# scraping people covid - 19 in Thailand
def covid_19_scraping():
    url = 'https://covid19.th-stat.com/api/open/today' # api for covid-19
    response = requests.request('GET', url)
    data = response.json()

    df = pd.DataFrame.from_dict(data, orient = 'index')
    # print all except last 3 data
    print(' Covid - 19 In Thailand')
    print(df[:-3])

covid_19_scraping() # call function


#สร้าง Line Notify ผ่าน script

URL = 'https://notify-api.line.me/api/notify'
Token ='ic23VahorgzkTy3iP2xZxfuZNsXFgYeiv2XGyJ36N6v'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+Token}
Message = 'Line Notify with Python, Hello Nattapong'
r = requests.post(URL, headers=headers , data = {'message':Message})
print(r.text)

'''