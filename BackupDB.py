import sqlite3
import io
from sqlite3 import Error
import datetime
import ftplib # move file with FTP

# ทดสอบ Backup DB SQLite 

# ทดสอบการสร้าง Connection
'''
def SQLiteBackup():
    try:
        con = sqlite3.connect('/Users/tou/Programming/SQLite/TestDB.db')
        print('Connection is successfully.')
        return con
    
    except Error:
        print(Error)
    
    finally:
        con.close()

SQLiteBackup()
'''


# ทดสอบการ Backup 
con = sqlite3.connect('/Users/tou/Programming/SQLite/TestDB.db')

with io.open('Database/BackupDB/BackupDB_dump'+ str(datetime.datetime.now()) +'.sql', 'w') as p: #เพิ่ม path directory folder
    for line in con.iterdump():
        p.write('%s\n' % line)

print('Backup Database is success !!')
con.close()




# move file with FTP (Upload)
# Fill Required Information
'''
HOSTNAME : "10.0.186.165" 
USERNAME :
PASSWORD :

#connect to FTP Server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)


'''
HOSTNAME = "http://demo.wftpserver.com/" 
USERNAME = "demo"
PASSWORD = "demo"
# Connect FTP Server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
# force UTF-8 encoding
ftp_server.encoding = "UTF-8"
# Enter File Name
file_name = "Database/BackupDB/BackupDB_dump2022-08-29 11:22:35.510608.sql"
# Read file in binary mode
with open(file_name, "rb") as file:
    ftp_server.storbinary(f"STORE {file_name}", file)

ftp_server.dir()
ftp_server.quit()


# move file with FTP (Download)
HOSTNAME = "http://demo.wftpserver.com/" 
USERNAME = "demo"
PASSWORD = "demo"
# Connect FTP Server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
# force UTF-8 encoding
ftp_server.encoding = "UTF-8"
# Enter File Name
file_name = "Database/BackupDB/BackupDB_dump2022-08-29 11:22:35.510608.sql"
# Read file in binary mode
with open(file_name, "wb") as file:
    ftp_server.retrbinary(f"RETR {file_name}", file.write)

ftp_server.dir()
ftp_server.quit()


