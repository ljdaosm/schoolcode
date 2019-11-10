import mysql.connector as sql
mycon=sql.connect(host='localhost',user='root',passwd='lj2002',database='ljdaosm')
cursor=mycon.cursor()
if mycon.is_connected:
    print('connection succesful')
    print()
a=input('enter/access/search: ')

#functions

def insert():
    a1=input('Enter itemcode:')
    a2=input('Enter itemname:')
    a3=int(input('Enter price:'))
    q="insert into item values('%s','%s','%f');" % (a1,a2,a3)
    cursor.execute(q)
    mycon.commit()
        
def access():
    q='select * from item;'
    cursor.execute(q)
    x=cursor.fetchall()
    for row in x:
        print(row)
        
def searchcode():
    a1=input('enter itemcode:')
    q='select * from item where itemcode="%s";' % (a1)
    cursor.execute(q)
    x=cursor.fetchall()
    for row in x:
        print(row)
        
#main

if a=='enter':
    insert()
elif a=='access':
    access()
elif a=='search':
    searchcode()
else:
    print('Error in input ')    
            























