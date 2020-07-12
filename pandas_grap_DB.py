# test Create Graph Data with pandas use data from  database
from pandas import *
import numpy
import matplotlib.pyplot as plt
import sqlite3

# ---- connect database -----
# connect database sqllit3 from in project

con = sqlite3.connect('Database/DB_Test.db')
con.cursor()
print('connected')  # connect complese

# ----------------------------
'''
sql_select = 'SELECT Date, Total_Price FROM Tb_Electric;'
rows = con.execute(sql_select)
for row_show in rows:
	print(row_show)
'''

query_sql = pandas.read_sql_query('SELECT Date_Pay, Total_Price FROM Tb_Electric', con)
df = pandas.DataFrame(query_sql, columns=['Date_Pay', 'Total_Price'])
df.plot(figsize=(10,6), marker='o',markersize=3, x='Date_Pay', y='Total_Price',color='red', grid=True)
plt.title("Eletric And Water Price Per Mount")
plt.xticks(rotation='90')
plt.show()
























