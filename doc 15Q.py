a=["python","list","exercises","practice","soluction"]
i=0
b=[]
while i<len(a):
    s=a[i][-1::-1]
    b.append(s)
    i=i+1
print(b)