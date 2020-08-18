import sqlite3
# connect database sqllit3 from in project

con = sqlite3.connect('Database/DB_Test.db')
con.cursor()
print('connected')  # connect complese

'''
# SQL Select from Database
sqlSelect = 'SELECT * FROM Tb_Name'
for row in con.execute(sqlSelect):
    # show all data in database
    # print(row)
    print('ID =', row[0])
    print('Name =', row[1])
    print('Tel =', row[2])
    print('Sex =', row[3])
    print('Username =', row[4])
    print('Password =', row[5])
    print('Status =', row[6],'\n')


# Insert Data to Database
sqlInsert = 'INSERT INTO Tb_Name (ID,Name,Tel,Sex,Username,Password,Status) \
    VALUES (7,"Wuttichai",0988888888,"Male","boey",1234,"User");'
con.execute(sqlInsert)
con.commit()
print('Insert complese')
con.close()

# Update Data in database from SQL command
sqlUpdate = 'UPDATE Tb_Name SET Name="Kattiya" WHERE ID=7;'
con.execute(sqlUpdate)
con.commit()
con.close()


# Delete data in Database
sqlDelete = 'DELETE  FROM Tb_Name WHERE ID=7;'
con.execute(sqlDelete)
con.commit()
con.close()

'''
