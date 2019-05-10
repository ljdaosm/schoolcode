f=open("myfile.txt","r")
# (i)
a=f.read()
x=a.split()

print("Number of words:",len(x))

#(ii)

ct=0
f.seek(0)
for word in x:
    if x.count(word)==1:
        ct+=1
print("Number of different words are:",ct)   

#(iii) 

z=0
d={}
for word in x:
    if x.count(word)!=1:
        z=x.count(word)
        d[word]=z
print(max(d.values()))
print()



#(b)


f.seek(0)
d1={}
b=f.read().split()
for word in b:
    c=len(word)
    e=word
    d1[e]=c
print(d1)

print()

l2=[]
def filter_longest_words(n):
    f.seek(0)
    for word in b:
        if len(word)>=n:
            l2.append(word)
    print(l2)       
n=int(input("Enter the word length: "))           

filter_longest_words(n)    

for word in l2:
    b.remove(word)
print (b)    
            
        
