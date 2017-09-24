a=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
b=int(input("input a number:"))
a.append(b)
l=len(a)
for i in range(l-1,-1,-1):
    if a[i]>a[i-1]:break
    else:a[i],a[i-1]=a[i-1],a[i]
print(a)
