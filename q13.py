f=open("q13.txt","r")
f2=open('q13o.txt','w')


def isvowel():
    a=f.read()
    c=a.split()
    for word in c:
        
        if word[0] not in "AEIOUaeiou":
            b=word
            f2.write(b+" ")
            print(word)
            
isvowel()            
            