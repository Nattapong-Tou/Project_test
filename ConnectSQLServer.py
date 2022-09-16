

import pyodbc
import os


server_intra = '10.0.105.145'
server_remote = '198.168.37.27'
port = '1433'
database = 'SolarWindsOrion'
username = 'sa'
password = 'P@ssw0rd'
connection_str = r''

print(pyodbc.drivers())
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server_intra, port+';DATABASE='+database+';UID='+username+';PWD='+ password)

conn = pyodbc.connect(
        driver="ODBC Driver 17 for SQL Server",
        server="10.0.105.145",
        port=1433,
        database="SolarWindsOrion",
        uid="sa",
        pwd="P@ssw0rd",
        sslmode=True,
        timeout=1,
    )
cursor = conn.cursor()

cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()


    
    



'''
# check drivers for connect database
print(pyodbc.drivers())

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server_intra+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()



connection = pyodbc.connect(
        driver="ODBC Driver 17 for SQL Server",
        server="127.0.0.1",
        port=10022,
        database=os.environ["DB_NAME"],
        uid=os.environ["DB_USER"],
        pwd=os.environ["DB_PASS"],
        sslmode=True,
        timeout=1,
        attrs_before={SQL_ATTR_CONNECTION_TIMEOUT_ID: 1},
    )

connection = pyodbc.connect(
    driver="ODBC Driver 17 for SQL Server",
    server=os.environ["DB_HOST"],
    port=int(os.environ["DB_PORT"]),
    database=os.environ["DB_NAME"],
    uid=os.environ["DB_USER"],
    pwd=os.environ["DB_PASS"],
    sslmode=True,
)


'''












