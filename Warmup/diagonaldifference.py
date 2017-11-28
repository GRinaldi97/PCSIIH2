#!/bin/python3

import sys


n = int(input().strip())
a = []
n1=0
n2=0
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
for x in range(n):
    n1+=a[x][x]
    n2+=a[x][n-1-x]
print(abs(n2-n1))