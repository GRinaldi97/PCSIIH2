# Enter your code here. Read input from STDIN. Print output to STDOUT
import string
s=input().split()
a=set()
for x in s:
    for w in x:
        a.add(w.lower())
if a==set(string.ascii_lowercase):
    print("pangram")
else:
    print("not pangram")
