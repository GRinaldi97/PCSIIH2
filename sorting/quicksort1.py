n,k =int(input()),input().split()
left=[]
equal=[]
right=[]
for x in k:
        if int(x)< int(k[0]):
            left.append(x)
        if int(x)==int(k[0]):
            equal.append(x)
        if int(x)>int(k[0]):
            right.append(x)
print (" ".join(left+equal+right))