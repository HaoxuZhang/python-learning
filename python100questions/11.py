f1=1
f2=1
print("%12ld" %f1,end=' ')
for i in range(2,24):
	print("%12ld" %f2,end=' ')
	f1,f2=f2,f1+f2
	if i%6==0: print()
print()
