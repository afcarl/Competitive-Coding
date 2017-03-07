#!/bin/python3

import sys
import re

s = input().strip()
def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
b=convert(s)
a=b.split("_")
#print (a)
print (len(a))