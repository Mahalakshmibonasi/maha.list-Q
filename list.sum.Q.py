a=[[1,2,3],[3,4,5,6],[7,8,9,1],[11,3,45,]]
b=[]
i=0
while i<len(a):
      j=0
      sum=0
      while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
      b.append(sum)
      i=i+1
print(b)