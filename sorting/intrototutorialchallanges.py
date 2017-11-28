ElementToFind= int(input())
SizeArray= int(input())
ar=list(map(int,input().split()))
L=([pos for pos, char in enumerate(ar) if char==ElementToFind])
for x in L:
    print (x),
