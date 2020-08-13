# ทดสอบ Auto run script
import schedule
def test_schedule():
    print('Hello Nattapong')

schedule.every(5).seconds.do(test_schedule)
schedule.run_pending()


'''
***** Example code for auto run python script

from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    print "hello world"
    #...

t = Timer(secs, hello_world)
t.start()


import datetime
from threading import Timer
x = datetime.datetime.today()
print(x)

'''