n=int(input())
count=0
ar= list(map(int,input().split()))
for i in range(1,len(ar)):
    key = ar[i]
    j = i-1
    while j >= 0 and key<ar[j] :
        ar[j +1] = ar[ j ]
        j -= 1
        count+=1
    ar[j+1] = key
print (count)