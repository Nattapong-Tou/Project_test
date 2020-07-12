import pypyodbc as pyodbc # liberties for connect database MS SQL Server

print('test connect ms sql server')

server = '172.168.10.140'
database = 'SolarWindsOrion'
username = 'sa'
password = 'P@ssw0rd'
connection_string = 'Driver={SQL Server};' \
                    'Server='+ server +';Database='+ database +';UID='+ username +';PWD='+ password +';'
con = pyodbc.connect(connection_string)
con.cursor()

'''
sqlconnection = pypyodbc.connect("Driver={OOBC Driver 13 for SQL Server};",
								 "Server=172.168.10.140;",
								 "Database=SolarWindsOrion;",
								 "uid=sa;",
								 "pwd=P@ssw0rd")

cursor = sqlconnection.cursor()

con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};',
                     SERVER='172.169.10.140')

'''

