n=int(input())
k=list(map(int,input().split()))
r=list(sorted(k))
print(r[(len(k)-1)//2])