f=open("Q13.txt")
i=0
s=""
a=f.read()
b=a.split()
l=list(b)
l1=[]
for word in l:
    if word[0] not in "AEIOUaeiou":
        l1.append(word)
for i in l1:
    s=i + " "+s


f.close()

f=open("file2.txt","w")
f.write(s)
f.close()        
        
        
    
    

