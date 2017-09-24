a=[1,2,3,4,5,6,7]
#方法一:
l=len(a)
for i in range(int(l/2)):
    a[i],a[l-i-1]=a[l-i-1],a[i]
print(a)
#方法二:
b=[1,2,3,4,5,6,7]
print(b[::-1])
