#สร้าง Line Notify ผ่าน script
import requests

URL = 'https://notify-api.line.me/api/notify'
Token ='ic23VahorgzkTy3iP2xZxfuZNsXFgYeiv2XGyJ36N6v'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+Token} 
payload = {'message' : "Hello.\n Nattapong \n test"
    ,'notificationDisabled' : True
    , 'stickerPackageId' : '446' # ส่ง Stiker
    , 'stickerId' : '2024' # ส่ง Stiker
}
#Message = {"Test Notify."}
r = requests.post(URL, headers=headers, params=payload)
print(r.text)

#Test Token : ic23VahorgzkTy3iP2xZxfuZNsXFgYeiv2XGyJ36N6v
