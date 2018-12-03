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

cols = [x[0] for x in cursor.description]

print cols

json_data = []

for d in data:
        json_data.append(dict(zip(cols,d)))

print json_data


jsonFormatData = json.dumps(json_data, indent=4, sort_keys=True)


print jsonFormatData
# for i in data:
#     print i[0],"-",i[1],"-",i[2],"-",i[3]

# print data
#
# json_data = dict(data)

# print json_data
#
# for i in data:
#         print i

# print json_data

# print dict(data)
cnxn.close()