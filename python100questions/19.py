for i in range(1,1001):
	total=0
	for j in range(1,i):
		if i%j==0:
			total=int(total+j)
	if total==i:
		print(i)
