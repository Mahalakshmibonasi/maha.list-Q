# a=int(input("enter a num"))
# i=0
# b=[]
# while i<a:
#     n=int(input("enter a num"))
#     b.append(n)
#     i=i+1
# print

# a=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         print(a[i],"even num")
#     else:
#         print(a[i],"odd num")
#     i=i+1

# a=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# sume=0
# sumo=0
# while i<len(a):
#     if a[i]%2==0:
#         sume=sume+a[i]
#     else:
#         sumo=sumo+a[i]
#     i=i+1
# print("sum of even num",sume)
# print("sum of odd num",sumo)

# a=["a","n","t","a","a","t","n","n","a","x","u","g","a","a","x","a"]
# i=0
# b=[]
# while i<len(a):



# a=["the","quick","fox"]
# i=0
# j=" "
# r="dog"
# while i<len(a):
#     if a[i]=="fox":
#         j+=r+" "
#     else:
#         j+=a[i]+" "
#     i=i+1
# print(j)


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

# a=[1,2,3,4,5,1,2,3,4]
# b=[]
# i=0
# while i<len(a):
#     k=a[i]
#     if k not in b:
#         b.append(a[i])
#     i=i+1
# print(b)

# a=["maha",12,12.3,"c++"]
# b=[]
# i=0
# while i<len(a):
#     if type (a[i])==str:
#         b.append(a[i])
#     i=i+1
# print(b)

# n=int(input("enetr the num"))
# b=[]
# i=0
# while i<n:
#     a=int(input("enter the num"))
#     b.append(a)
#     i=i+1
# print(b)

# a=[1,2,3,4,5,6,7]
# i=0
# max=0
# while i<len(a):
#     if a[i]>max:
#         secondmax=max
#         max=a[i]
#     i=i+1
# print(secondmax)

# a=[1,2,3,4,5,6,7,8]
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         print(a[i],"even num")
#     else:
#         print(a[i],"odd num")
#     i=i+1

# a=[1,2,3,4,5,6,7,8,9]
# i=0
# sume=0
# sumo=0
# while i<len(a):
#     if a[i]%2==0:
#         sume=sume+a[i]
#     else:
#         sumo=sumo+a[i]
#     i=i+1
# print("sum of the",sume)
# print("sum of the",sumo)

# a=[1,2,3,4,5,6]
# b=[10,20,30,40,50,60]
# # c=[]
# i=0
# b.reverse()
# while i<len(a):
#     print(a[i],b[i],end=",")
#     # c.append(a[i])
#     i=i+1
# # print(c)

# a=["maha","lakshmi","navgurukul","campus"]
# i=len(a)-1
# b=[]
# while i>0:
#     b.append(a[i])
#     b.append(a[i-3])
#     i=i+2
# print(b)

# a=[1,2,[],4,[],5,[],6]
# b=[]
# i=0
# while i<len(a):
#     if type(a[i])!=:
#         b.append(a[i])
#     i=i+1
# print(b)


# a=[2,3,5,[3,2],[1,2],3,2]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a):
#         sum=sum+a[i]
#     j=j+1
#     b.append(sum)
# i=i+1
# print(b)


# a=[2,3,5,[3,2],[1,2],3,2]
# i=0
# b=[]
# sum=0
# while i<len(a):
#     if a[i]==list:
#         b.append(a[i])   
#         # j=0
#         # while j<len(a[i]):
#         #     j=j+1
#         # sum=+(a[i])
#         sum=sum+a[i]
#     i=i+1
# print(sum)
# print(b)


# a=[2,3,5,[3,2],[1,2],3,2]
# i=0
# sum1=0
# sum2=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum1+=a[i][j]
#             j+=1
#     else:
#         sum2+=a[i]
#     i+=1
# print(sum1)
# print(sum2)
# print(sum1+sum2)
    

# a=[2,3,5,[3,2],[1,2],3,2]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum+=a[i][j]
#             j+=1
#     else:
#         sum+=a[i]
#     i+=1
# print(sum)
    
# a=[1,5,3,1,5,3,2]
# b=[]
# i=0
# while i<len(a):
#     if a[i] not in b:
#         b.append (a[i])
#     i=i+1
# print(b)


# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print(i,end="")
#         j=j+2
#     print()
#     i=i+2

i=1
while i<=4:
    j=0
    while j<=i:
        print(j*j,end="")
        j=j+1
    print()
    i=i+1