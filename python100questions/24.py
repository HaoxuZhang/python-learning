a,b=2,1
res=a/b
for i in range(1,20):
    a,b=a+b,a
    res+=a/b
print(res)
