a=[1,0,2,0,3,0,4,0,5]
i=0
b=[]
c=[]
while i<len(a):
    if a[i]!=0:
        b.append(a[i])
    else:
        c.append(a[i])
    i=i+1
print(b+c)