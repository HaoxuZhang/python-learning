num=int(input("请输入一个数字:"))
n=int(input("您希望将上述数字相加几次:"))
res=0
tmp=num
for i in range(n):
	res+=num
	num=int(num*10+tmp)
print(res)
