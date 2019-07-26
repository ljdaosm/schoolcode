from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("LOAN SIMPLE INTEREST CALCULATOR")
p=StringVar()
r=StringVar()
t=StringVar()

Label(root, text="Enter principal amount: ").grid(column=0, row=0)
Entry(root, textvariable=p).grid(column=1, row=0)

Label(root, text="Enter rate: ").grid(column=0, row=1)
Entry(root, textvariable=r).grid(column=1, row=1)

Label(root, text="Enter loan duration: ").grid(column=0, row=2)
Entry(root, textvariable=t).grid(column=1, row=2)

def click():
    P=int(p.get())
    R=int(r.get())
    T=int(t.get())
    SI=(P*R*T)/100
    messagebox.showinfo("PROMPT!!!", "Your interest amount is: "+str(SI))
    
    messagebox.showinfo("PROMPT2!!!!", "HAHAHAHAHAHAHAHAHA")

Button(root, text="Calculate interest", command=click).grid(column=0, row=5)

Button(root, text="Not interested", command=root.destroy).grid(column=1, row=5)


root.mainloop()

     
    
