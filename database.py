import pyodbc

cnxn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=trngsql.ajrgroup.in;'
        'DATABASE=Aravind;'
        'UID=sa;'
        'PWD=Welcome@123'
                      )
print "connected"

cursor = cnxn.cursor()

cursor.execute("select * from customerdata")
for i in cursor.fetchall():
    print i[0],'-',i[1],'-',i[2],'-',i[3]

cnxn.close()
