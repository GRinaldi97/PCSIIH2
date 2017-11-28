n=int(input())
l=list(map(int,input().split()))
H=[]
for x in range(100):
    H.append(l.count(x))
H=list(map(str, H))
print (" ".join(H))