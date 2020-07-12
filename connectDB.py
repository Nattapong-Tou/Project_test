import sys
print(sys.version)
'''
def connect_mysql():
        con = mysql.connector.connect(host='localhost', port='8080',
                                      database='TestDatabase',
                                      user='root',
                                      password=' ')
        cursor = con.cursor()
        cursor.execute('SELECT VERSION()')
        data = cursor.fetchone()
        con.close()
        print('Connect Ok')

'''




'''
db = pymysql.connect('localhost','root','','TestDatabase')
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print('Database version : ',data)
db.close()


hostname = 'localhost'
username = 'root'
password = ''
db = 'TestDatabase'

con=pymysql.connect(host=hostname,
        database=db,
        user=username,
        password=password)
mycursor = con.cursor()
#---------------------------------------------------------------------
'''
'''
try:
    connection = mysql.connector.connect(
        host='localhost',
        port = '8080',
        database='TestDatabase',
        user='root',
        password=' '
    )
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        cursor = connection.cursor()
        cursor.execute("Testdatabase();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)

except EOFError as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#---------------------------------------------------------------------

'''
