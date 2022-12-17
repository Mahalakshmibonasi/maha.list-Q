# a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# i=0
# min=1
# max=0
# n=[]
# k=[]
# while i<len(a):
#     if max<len(a[i]):
#         max=len(a[i])
#         n=a[i]
#     if min>len(a[i]):
#         min=len(a[i])
#         k=a[i]
#     i=i+1
# print(max,n)
# print(max,k)

# list=["flour","chees","carrots"]
# b=len(list)
# i=0
# while i<b:
#     print(i,":",list[i])
#     i=i+1

a=int(input("enetr the num"))
i=0
b=[]
while i<a:
    c=int(input("enter the num"))
    b.append(c)
    i=i+1
print(b)