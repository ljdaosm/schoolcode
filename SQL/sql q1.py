#table creation
import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",passwd="lj2002",database="ljdaosm")
cursor=mycon.cursor()

if mycon.is_connected():
    print("connection succesful")
    
    
#(i)    
cursor.execute('select teacher.name, salary.da from teacher,salary where teacher.sid=salary.sid and teacher.dept="accounts" and teacher.experience>10 and salary.da>300')
z=cursor.fetchall()

for row in z:
    print('output:')    

#(ii)
cursor.execute('select teacher.name, teacher.sid, salary.basic from teacher, salary where teacher.sid=salary.sid and teacher.dept="physics"')

x=cursor.fetchall()
print('output')
for row in x:
     print (row)
print()

#(iii)
cursor.execute('update teacher set experience=experience+2 where dept="computer"')     

#(iv)
cursor.execute('select min(basic), max(basic) from salary')
y=cursor.fetchall()
for row in y:
    print(row)

#(v)
cursor.execute('delete from salary')
mycon.commit()
    