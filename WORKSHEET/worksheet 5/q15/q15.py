f=open("my.txt")
f1=open("new.txt","w")
s=f.readlines()
l=len(s)
f.seek(0)
for i in range (0,l):
    z=f.readline()
    #for all upper case use upper()
    q=z.capitalize()
    f1.write(q)

f.close()
f1.close()