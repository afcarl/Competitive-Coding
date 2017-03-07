#!/bin/python3

import sys
import string


h = list(map(int, input().strip().split(' ')))
word = input().strip()

d={}
i=0
for count in h:
    d[chr(i+97)]=count
    i=i+1
max=0
for words in word:
    if max<d[words]:
        max=d[words]
print(max*len(word))
        
