n=int(input("Enter the line number needed"))
ct=1
f=open("q1.txt","w")
f.writelines("neither apple nor pine are in pineapple. boxing rings are square. \nwriters write, but fingers don't fing. overlook and oversee are opposite. \na house can burn up as it burns down. an alarm goes off by going on.")
f.seek(0,2)
f.writelines(" This is weird. \nSOS save us aaaaaa")
f.close()

f1=open("q1.txt")
l=f1.readlines()
a=len(l)
for ln in l:
    print(ct,":",ln)
    ct+=1
    
print(l[-1])
print("Line number",n,"is:",l[n-1])

f1.seek(10)
line=f1.readline()
print(line)



d={}
f1.seek(0)
for i in f1.readlines():
    for j in i.split():
        j = j.lower()
        if j[0] not in d:
            d[j[0]] = 1
        else:
            d[j[0]] += 1

for i in d.items():
    print("Words beginning with",i[0],":",i[1])
 



