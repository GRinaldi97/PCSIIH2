#!/bin/python3

import sys


n = int(input().strip())
for x in range(1,n+1): #to avoid upper spaces
    print (str("#"*x).rjust(n))