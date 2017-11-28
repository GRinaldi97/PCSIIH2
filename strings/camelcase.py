#!/bin/python3

import sys


s = input().strip()
counter=1
for x in s[1:]:
    if x.isupper():
        counter+=1
print(counter)
