#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    n=str(s) 
    L=[]
    result="NO"
    x_value=''
    for x in range(1,len(n)):
        L.append(n[0:x])
    for x in L:
        w=0
        H=""
        while len(H)<=len(n):
            H+=str(int(x) + w)
            w+=1
            if len(H)==len(n) and H==n:
               result="YES"
               x_value=x
               break 
    print (result, x_value)    