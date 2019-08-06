import math 
import matplotlib.pyplot as plt

print("First function is: f1(t)= ((c**(-t))+(2*pi*t)")
print("Second function is: f2(t)=cos(2*pi*t)")

t=int(input("enter value of t:"))
c=int(input("Enter value of c:"))

l1=[]
l2=[]
l3=[]

for i in range(0,t):
    y=math.cos(2*math.pi*i)
    x=(c**(-t)+ (2*math.pi*i))
    l1.append(x)
    l2.append(y)
    l3.append(i)
    

plt.plot(l3,l1,label="f(1)",color="red",marker="v")
plt.plot(l3,l2,label="f(2)",color="k",marker="o")
plt.legend(loc=2)
plt.title("Graph for the values of f(1) and f(2)")
plt.xlabel("values of t")
plt.ylabel("values of function")

