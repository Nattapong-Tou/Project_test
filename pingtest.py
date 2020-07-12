import csv
import subprocess
import socket
import sys
import scapy
import os
# import libraly for use

print('your scapy version is',scapy.VERSION)
'''
# script ping for example 2 easy script

hostname1=' 8.8.8.8 '
respone = os.system("ping" + hostname1)

if respone == 0:
	print(hostname1,': is Up.')
else :
	print(hostname1, 'is Down.')

# this scrip running infinity press control + c for stop
# scrip ping complease nex example read IP from notepad for ping
'''

#example read ip address from txt file
hostname2 = open('file/ip_address.txt', mode='r+', encoding='UTF-8') # read file from location
print(hostname2.read()) # read file OK.



''' 
# Script Ping For Example 1 read form Excel

def ping(hostname):
	p = subprocess.Popen('ping', + hostname, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	pingStatus = 'ok';

	for line in p.stdout:
		output = line.rstrip().decode('UTF-8')

		if (output.endswith('unreachable.')):
			#No route from the local system. Packets sent were never put on the wire.
			pingstatus = 'unreachable.'
			break

		elif (output.startswith('Ping request could not find host')) :
            pingStatus = 'host_not_found'
            break


        if (output.startswith('Request timed out.')) :
            #No Echo Reply messages were received within the default time of 1 second.
            pingStatus = 'timed_out'
            break

    return pingstatus



def printPingResult(hostname):
    statusOfPing = ping(hostname)
    
    if (statusOfPing == 'host_not_found') :
        writeToFile('!server-not-found.txt', hostname)
    elif (statusOfPing == 'unreacheable') :
       writeToFile('!unreachable.txt', hostname)
    elif (statusOfPing == 'timed_out') :
       writeToFile('!timed_out.txt', hostname)	   
    elif (statusOfPing == 'ok') :
        writeToFile('!ok.txt', hostname)
    #endIf
#endPing


def writeToFile(filename, data) :
    with open(filename, 'a') as output:
        output.write(data + '\n')
    #endWith
#endDef    

   #servers.txt example
   #vm8558
   #host2
   #server873
   #google.com

file = open('servers.txt') 

try:
    reader = csv.reader(file)
    
    for item in reader:
        printPingResult(item[0].strip())
    #endFor
finally:
    file.close()
#endTry

'''







