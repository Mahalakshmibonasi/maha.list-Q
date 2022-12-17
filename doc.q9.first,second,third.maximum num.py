# a=[50,40,23,70,56,12,5,10,7]
# fm=0
# sm=0
# tm=a[0]
# i=0
# while i<len(a):
#     if a[i]>fm:
#         fm=a[i]
#     if a[i]>sm and a[i]!=fm:
#         sm=a[i]
#     if a[i]>tm and a[i]!=fm and a[i]!=sm:
#             tm=a[i]
#     i=i+1
# print(fm,sm,tm)



# i=0
# a=0
# while i<len(list):
#     if list[i]>a:
#         a=list[i]
#     i=i+1
# print(a)
# i=0
# b=0
# while i<len(list):
#     if list[i]>b:
#         if list[i]!=a:
#             b=list[i]
#     i=i+1
# print(b)
# i=0
# c=0
# while i<len(list):
#     if list[i]>c:
#         if list[i]!=a and list[i]!=b:
#             c=list[i]
#     i=i+1
# print(c)

# list=[1,2,3,1,2,3,4,5,6]
# i=0
# n=[]
# while i<len(list):
#     if list[i]not in n:
#         n.append(list[i])
#     i=i+1
# print(n)


# i=5
# while i>=1:
#     j=5
#     while j>=1:
#         print(i,end=" ")
#         j=j-1
#     print()
#     i=i-1

# i=1
# while i<=5:
#     j=5
#     while j>=i:
#         print(j,end=" ")
#         j-=1
#     print()
#     i+=1

# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j+=1
#     print()
#     i-=1


# from operator import index
# from re import I


# a=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
# b=[]
# i=0
# c=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# print(c)

# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i=i+1
# print(b)


# m=[10,32,42,65,67,89,76,38,67]
# i=0
# sum=0
# while i<len(m):
#     sum=sum+a[i]
#     i=i+1
# print(sum,i)

# a=["jyothi","raj","110"]
# print(a[0]+" "+a[1]+" "+a[2])


# a=["maha","swathi","triveni"]
# i=len(a)-1
# while i<0:
#     print(i)
#     i=i-1



# a=["jyothi","raj","arjun","sanvi"]
# i=0
# b=[]
# while i<len(a):
#     print(i,":",a[i])
#     i=i+1



# a=["g","f","g"]
# b=[]
# i=0
# while i<len(a):
#     b.append(a[i])
#     i=i+1
# print(b)


# a=[1,2,3,4,5,6]
# b=["jyothi"]
# i=0
# s=[]
# while i<len(a):
#     s=(a[i],b[i])
#     s.append (a[i])
#     # s.append (b[i])
#     i+=1
# print(s)


# a=[1,2,2,5,8,4,4,8]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i=i+1
# print(b)


# a=[6,1,3,5,6,3,1]
# i=0
# b=[]
# p=1
# while i<len(a):
#     if a[i]not in b:
#         b.append(a[i])
#         p=p*b[i]
#     i=i+1
# print(p)

# a=[1,2,3,4,5,6,7]
# fstmax=0
# secmax=0
# thimax=0
# i=0
# while i<len(a):
#     if a[i]>fstmax:
#         fstmax=a[i]
#     if a[i]>secmax and a[i]!=fstmax:
#         secmax=a[i]
#     if a[i]>thimax and a[i]!=fstmax and a[i]!=secmax:
#         thimax=a[i]
#     i=i+1
# print(fstmax,secmax,thimax)


# fruits=["banana","apple","mango"]
# print(fruits[:-1])

# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(fruits[3:6])
