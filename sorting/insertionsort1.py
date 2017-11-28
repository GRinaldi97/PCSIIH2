n=int(input())
Arr= list(map(int,input().split()))
e= Arr[-1]
for x in range(len(Arr)-1)[::-1]:
    if Arr[x]>e:
        Arr[x+1]=Arr[x]
        print(" ".join(map(str,Arr)))
    if Arr[x]<e:
        Arr[x+1]=e
        print (" ".join(map(str,Arr)))
        break
    if x==0:
        Arr[0]= e
        print (" ".join(map(str,Arr)))