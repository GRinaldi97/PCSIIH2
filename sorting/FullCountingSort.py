n=int(input())
L=list()
L2=list()
for x in range(n):
    num, k = input().split()
    if x in range(n//2):
        L.append((int(num), "-"))
    else:
        L.append((int(num), k))
for x in (sorted(L, key=lambda x: x[0])):
        L2.append(x[1])
print (" ".join(L2))
     
    