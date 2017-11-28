#!/bin/python3

import sys

def funnyString(s):
    r=s[::-1]
    if all(abs(ord(s[i])-ord(s[i-1]))==abs(ord(r[i])-ord(r[i-1])) for i in range(len(s))):
        return("Funny")
    else:
        return("Not Funny")

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)