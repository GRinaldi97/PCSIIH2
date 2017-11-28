#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
positive=0
negative=0
zeros=0
for x in arr:
    if x>0:
        positive+=1
    if x<0:
        negative+=1
    if x==0:
        zeros+=1
print (round(positive/n, n))
print (round(negative/n, n))
print (round(zeros/n, n))