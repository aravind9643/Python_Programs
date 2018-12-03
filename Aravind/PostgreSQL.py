import psycopg2

i=1
conn = psycopg2.connect("dbname=postgres user=postgres")
print "connected successfully"
cursor = conn.cursor()
print "cursor opened successfully"
# sql = "insert into Aravind(id, name) values(%s, %s)"
# # data = (101,'Shiva')
# mylist = [(101,'aravind'),(105,'Ramana')]
# while i==1:
#     id = input("Enter Id")
#     name = raw_input("Enter Name")
#     mytuple = (id,name)
#     mylist.append(mytuple)
#     c = raw_input("add one more")
#     if (c == "y"):
#         i = 1
#     else:
#         i = 0
#     # cursor.execute("insert into Aravind(id, name) values(102,'Raghava')")
# cursor.executemany(sql,mylist)
# conn.commit()
# print cursor.rowcount," records inserted and last row id : ",cursor.lastrowid

sql = "delete from Aravind where id = %s"

id = input("Enter id")
data = (id)

cursor.execute(sql,data)

print cursor.rowcount, " records deleted"

cursor.execute("select * from Aravind")
details =  cursor.fetchall()

for i in details:
    print i[0],'-',i[1]
conn.close()
# print "done"