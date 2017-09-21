'''
这道题目要求分解成质因数，那么就从2开始，如果能整除n，那么就整除n，如果不行，
就继续往下循环，在range(2,n+1)中找，index一定是个质数，因为假如不是质数，在
这之前早就被除到过了，比如说，index不可能等于4,因为4可以被前面的2整除，n如果能被4整除，那么一定能被之前的2整除
'''
def num(m):
	n=int(m)
	print("{}=".format(n),end='')
	while n!=1:
		for index in range(2,n+1):
			if n%index==0:
				n=int(n/index)
				if n==1:
					print(index)
				else:
					print("{}*".format(index),end='')
				break
	return
n=int(input("请输入一个正整数："))
num(n)

