#สร้าง Line Notify ผ่าน script
import requests

URL = 'https://notify-api.line.me/api/notify'
Token ='ic23VahorgzkTy3iP2xZxfuZNsXFgYeiv2XGyJ36N6v'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+Token} 
Message = 'Line Notify with Python, Hello Nattapong'
r = requests.post(URL, headers=headers , data = {'message':Message})
print(r.text)

