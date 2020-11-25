import socket
import sys
import time
import speedtest
import inspect
# import libralies

server = ['https://www.speedtest.net/speedtest-servers']

s = speedtest.Speedtest()
for method in inspect.getmembers(s, predicate=inspect.ismethod):
    print(method)

print('my download is:', s.download())