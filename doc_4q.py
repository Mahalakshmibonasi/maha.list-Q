a=[6,1,3,5,6,3,1]
i=0
b=[]
p=1
while i<len(a):
    if a[i]not in b:
        b.append(a[i])
        p=p*b[i]
    i=i+1
print(p)