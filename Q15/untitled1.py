# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:22:17 2019

@author: SCL1
"""
#Question 8
a=int(input("speed"))
b=int(input("Is it your bithday (1=yes) ( 2=no)"))
if(b==1):
    if(60<=a):
        print("0")
    if(61<=a<=80):
        print("1")
    if(a<=85):
        print("2")
else:
    a=(a+5)

