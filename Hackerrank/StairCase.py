#!/bin/python3

import sys


n = int(input().strip())
def  StairCase(n):
    i=0
    for i in range(0,n):
      j=i
      if i!=n-1:  
        for j in range(0,n-j-1):
            print (" ",end="")
            
        for x in range(0,n-j-1):
            print ("#",end="")
      else:
        for x in range(0,n):
            print("#",end="")
      print ()
StairCase(n)