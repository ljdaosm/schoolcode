f=open("q14.txt")
l1=[]

a=f.readlines()
for i in range(0,len(a)):
    for word in str(i):
        x=a[i].split()
        l1.append(tuple(x))
print(l1)
print()
print()

for tup in l1:
    y=int(tup[3])
    if y<3:
        print(tup[0],tup[1],":no of years:",y)
    

