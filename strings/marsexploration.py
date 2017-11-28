#!/bin/python3

import sys


S = input().strip()
a = [S[i:i+3] for i in range(0, len(S), 3)]
counter=0
for x in a:
    if x[0] is not "S":
        counter+=1
    if x[1] is not "O":
        counter+=1
    if x[2] is not "S":
        counter+=1
print(counter)