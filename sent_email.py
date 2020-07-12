# import libraries for sent email
import smtplib
# connect mail server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("nattapongngamphak@gmail.com", "tou170135")
# sent email data
from_email = "nattapongngamphak@gmail.com"
to_email = "nattapong.ng@tot.co.th"
subject = "Test sent Email with python"
message = "Hello Nattapong, are you ok?"

#server.sendmail("nattapongngamphak@gmail.com", "nattapong.ng@tot.co.th", "Hello Nattapong")
server.sendmail(to_email, from_email, message)
# close connection
server.quit()
# code  ด้่้านบนสามารถทำงานได้แล้ว ต่อไปจะลองสร้างหน้า form เพื่อรับค่าแล้วส่ง email 

