flag=True
while flag==True:
    n=int(input("请输入一个数，如果它的平方小于50,程序将终止:"))
    if n*n>=50:flag=True
    else:flag=False
    print("该数的平方是:",n*n)
