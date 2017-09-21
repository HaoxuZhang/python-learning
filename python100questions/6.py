def fib1(n):
	if n==0:
		return 0
	if n==1:
		return 1
	return fib1(n-1)+fib1(n-2)
n=int(input("输出第几个fib数:"))
res=fib1(n)
print(res)
def fib2(m):
	if m==1:
		return [1]
	if m==2:
		return [1,1]
	fibs=[1,1]
	for i in range(2,n):
		fibs.append(fibs[-1]+fibs[-2])
	return fibs
m=int(input("你想输出几个fib数?:"))
resNum=fib2(m)
print(resNum)
