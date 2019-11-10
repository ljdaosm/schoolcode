import mysql.connector as sql
mycon=sql.connect(host='localhost',user='root',passwd='lj2002',database='ljdaosm')
if mycon.is_connected():
    print('connection succesful')
cursor=mycon.cursor()

cursor.execute('select watches.watch_name, watches.Qty_store from watches,sale where watches.watchid=sale.watchid and quarter=1')
x=cursor.fetchall()
for row in x:
    print(row)
print()
#(ii)

cursor.execute('select * from watches where watch_name like "%time"')
y=cursor.fetchall()
for row in y:
    print(row)
print()

#(iii)


cursor.execute('select Qty_store from watches where type="U"')    
a=cursor.fetchall()
for row in a:
    print(row)
print()

#(iv)
cursor.execute('select watch_name, price from watches where price>5000 and price<15000')
b=cursor.fetchall()
for row in b:
    print(row)
print()

#(v)
cursor.execute('select watchid, sum(Qty_sold) from sale group by watchid')
c=cursor.fetchall()
for row in c:
    print(row)    
    