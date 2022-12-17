# a=[1,0,2,0,3,0,4,0,5,0,6,0,]
# i=0
# b=[]
# while i<len(a):
#     if a[i]!=0: 
#         b.append(a[i])
#     i=i+1
# print(b)

# a=[34,67,12,-94.89,'python',0,'C++']
# b=[]
# i=0
# while i<len(a):
#     if type(a[i])==str:
#         b.append(a[i])
#     i+=1
# print(b)

# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
# b=[]
# i=0
# while i<len(a):
#     if a[i]==13 or a[i]==14 or a[i]==15 or a[i]==16 or a[i]==17:
#     # if a[i]>12 and a[i]<18:
#         b.append(a[i])
    # i+=1
# print(b)

# a=[10,20,30,40]
# b=[100,200,300,400]
# c=[]
# i=0
# b.reverse()
# while i<len(a):
#     c.append([a[i],b[i]])
#     i=i+1
# print(c)

# a=[[0,1,2],[2,3,4],[3,4,5,6],[7,8,9,10,11],[12,13,14]]
# b=[]
# i=0
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j+=1
#     b.append(sum)
#     i+=1
# print(b)

# b=a[12:-5]
# print(b) 

# a=["maha","swathi","mahi","ashu"]
# i=len(a)-1
# while i>=0:
#     print(a[i],end=" ")
#     i=i-1


# a=[2,3,4,5,6,2,3,4]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum)



# a="my name is mahalakshmi"
# i=0
# while i<len(a):
#     if i==11:
#         print(i)
#     i+=1


# a=["nav","gurukul","pune","campus"]
# b=a[2:-1]
# c=a[3:]
# d=a[:-2]
# print(d+c+b)
# a=["nav","gurukul","pune","campus"]
# i=1
# g=[]
# while i<len(a):
#     g.append(a[i])
#     g.append(a[i-1])
#     i=i+2
# print(g)

# a=[[1,2,3],[3,4,5,6],[7,8,9,1],[11,3,45,]]
# b=[]
# i=0
# while i<len(a):
#       j=0
#       sum=0
#       while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#       b.append(sum)
#       i=i+1
# print(b)


# a=[50,40,23,70,56,12,5,10,7]
# i=0
# count=0
# while i<len(a):
#       if a[i]>=20 and a[i]<=40:
#             count=count+1
#       i=i+1
# print(count)

# a=[1,0,2,0,3,0,4,0,5]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]!=0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# print(b+c)

# def fun():
#     print("hi")
# fun()
# print("bye")

# print("hello")
# def fun(a):
#     a=10
#     return(a)
# print(a)
# b=fun(a)
# print(b)


# def fun(a):
#     i=0
#     b=[]
#     while i<len(a):
#         if a[i]>="a" and a[i]<="z":
#             print(a)
#     i=i+1
# fun("my@ name2 is# maha7lakshmi")

# a=[3,4,5,6,7,8]
# i=0
# max=0
# while i<len(a):
#     if a[i]>max:
    
#         secondmax=max
#         max=a[i]
#     i=i+1
# print(secondmax)


i=5
while i>=1:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i-1