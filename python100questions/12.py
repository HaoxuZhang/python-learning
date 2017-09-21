import math
flag=True
for i in range(101,201):
	tmp=int(math.sqrt(i))+1
	for j in range(2,tmp+1):
		if i%j==0:
			flag=False
			break
	if flag==True:
		print(i)
	flag=True
