high=100.0
length=0.0
times=int(input("第几次反弹的结果:"))
for i in range(times):
	length+=high
	high=high/2
	length+=high
print("共经过{}米，第{}次反弹的高度为{}".format(length,times,high))
