n=int(input())
l=list(map(int,input().split()))
z= dict()
H=[]
for x in set(l):
    z[x]=l.count(x)
for x in z:
    for y in range(z[x]):
        H.append(x)
print (" ".join(list(map(str, H))))