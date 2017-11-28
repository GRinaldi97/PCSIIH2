#!/bin/python3

import sys

def timeConversion(s):
    L=s.split(":")
    if L[-1][-2:] =='AM':
        if L[0]=="12":
            L[0]="00"
        L[-1]= L[-1][:2]
    else:
        if (int(L[0]))==12:
            L[-1]= L[-1][:2]
        else:
            L[0] = str(int(L[0])+ 12)
            L[-1]= L[-1][:2]
    return ":".join(L)

s = input().strip()
result = timeConversion(s)
print(result)
