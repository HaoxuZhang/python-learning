def jiecheng(n):
    if n==1: return 1
    return n*jiecheng(n-1)
res=0
for i in range(1,21):
    res+=jiecheng(i)
print(res)
