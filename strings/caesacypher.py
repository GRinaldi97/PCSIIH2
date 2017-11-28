#!/bin/python3

import sys
import string

b=""
n = int(input().strip())
s = input().strip()
k = int(input().strip())
for x in s:
    if x.islower():
        if string.ascii_lowercase.index(x)+k <= 26:
            b += string.ascii_lowercase[(string.ascii_lowercase.index(x)+k)%26]
        if string.ascii_lowercase.index(x)+k > 26:
            b+= string.ascii_lowercase[(string.ascii_lowercase.index(x)+k)%26]
    if x.isupper():
        if string.ascii_uppercase.index(x)+k <= 26:
            b += string.ascii_uppercase[(string.ascii_uppercase.index(x)+k)%26]
        if string.ascii_uppercase.index(x)+k>26:
            b+= string.ascii_uppercase[(string.ascii_uppercase.index(x)+k)%26]
    if x.isalpha()==False:
        b+=x
print (b)
        
    
