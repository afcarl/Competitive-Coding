#!/bin/python3

import sys


time = input().strip()
y=time.split(":")
x=int(y[0])
if("PM" in y[2]):
    t=y[2].split("P")
else:
    t=y[2].split("A")
z=int(y[1])
r=int(t[0])
if ("AM" in y[2] and x==12):
    print ("00:"+format(y[1])+":"+format(t[0]))
  
elif("PM" in y[2] and x==12):
    print ("12:"+format(y[1])+":"+format(t[0]))
elif ("AM" in y[2] and x!=12):
    print ((format(y[0])+":"+format(y[1])+":"+format(t[0])))
elif ("PM" in y[2] and x!=12):
    q=x+12
    
    print (format(q)+":"+format(y[1])+":"+format(t[0]))
elif(x>12):
    print ("Invalid Input")