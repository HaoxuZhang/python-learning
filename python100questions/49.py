maximum=lambda x,y:(x>y)*x+(x<=y)*y #如果x>y，x>y的值为1,式子返回的是x，否则返回y
minimum=lambda x,y:(x>y)*y+(x<=y)*x #如果x>y，x>y的值为1,式子返回的是y，否则返回x
if __name__=='__main__':
    x=int(input("请输入第一个数比较大小:"))
    y=int(input("请输入第二个数比较大小:"))
print("the larger one is",maximum(x,y))
print("the lower one is",minimum(x,y))
