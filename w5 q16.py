f=open("studentdata.txt")
a=f.readlines()
ct=0
b=0
ma=0
mi=0

avg=0
for line in a:
    b=line.split()
    ct=0
    c=[int(n) for n in b[1:]]
    print(b[0],max(c), min(c))
 
            
            


               
    