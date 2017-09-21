def cube(n):
	return n*n*n
for i in range(100,1000):
	tmp=i
	total=0
	for j in range(0,3):
		total+=cube(tmp%10)
		tmp=tmp//10
	if total==i:
		print(i)
