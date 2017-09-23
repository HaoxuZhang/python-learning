def jiecheng(n):
    if n==1:return 1
    return n*jiecheng(n-1)
n=int(input("请输入数字："))
res=jiecheng(n)
print("该数字的阶乘是：",res)
