l=[]
for i in range(10):
    l.append(int(input("请输入一个数字:")))
l.sort()
for i in range(10):
    print(l[i])
n=iter(l)
for i in n:
    print(i)
