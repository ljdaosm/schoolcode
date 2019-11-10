import mysql.connector as sql
mycon=sql.connect(host='localhost',user='root',passwd='lj2002',database='ljdaosm')
cursor=mycon.cursor()
if mycon.is_connected():
    print('connection succesful')
    
a=input('Enter or Update ?? :').lower()


def enter():
    r = int(input("Roll no: "))
    n = input("Name: ")
    c = int(input("Class: "))
    dob = int(input("Date of birth: "))
    g = input("Gender: ")    
    q = "insert into student values('%d', '%s', '%d', '%d', '%s');" % (r, n, c, dob, g)
    cursor.execute(q)
    mycon.commit()

def update():
    r = int(input("Roll no: "))
    n = input("Name: ")
    c = int(input("Class: "))
    dob = int(input("Date of birth: "))
    g = input("Gender: ")    
    q="update student set name='%s', Class='%d', DOB='%d', Gender='%s' where roll='%d';" % (n,c,dob,g,r)
    cursor.execute(q)
    mycon.commit()
    
if a=="enter":
    enter()

elif a=="update":
    update()
    
else:
    print('incorrect entry')
    
        
    
    