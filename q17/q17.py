import urllib as ub
t=ub.request.urlopen("https://www.pythonforbeginners.com/")

print(t.headers)
x=t.headers

f=open("downloaded.htm","w")
f.write(str(t.read()))
f.close()

