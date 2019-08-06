f=open("story.txt")
a = f.read()
c=list(a)
b=""
d={}
l=[]
for i in range(0,len(a)):
    b=c[-1]
    c.pop()
    c.insert(0,b)
    
    x=""
    for letter in c:
        x+=letter
    l.append(x)
    
d[a]=l
print(d)        
        
    
    

