import pyodbc
import json
cnxn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=trngsql.ajrgroup.in;'
        'DATABASE=Aravind;'
        'UID=sa;'
        'PWD=Welcome@123;'
        )
cursor = cnxn.cursor()
cursor.execute("select * from customerdata")
data = cursor.fetchall()

#getting columns
cols = [x[0] for x in cursor.description]

print cols

json_data = []

#making dictionary
for d in data:
        json_data.append(dict(zip(cols,d)))

print json_data

#converting to json format
jsonFormatData = json.dumps(json_data, indent=4, sort_keys=True)

print jsonFormatData

cursor.close()
cnxn.close()