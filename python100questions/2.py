i=int(input("请输入当月利润："))
lirun=[1000000,600000,400000,200000,100000,0]
ticheng=[0.01,0.015,0.03,0.05,0.075,0.1]
sum=0
for j in range(0,6):
    if i>lirun[j]:
        sum+=(i-lirun[j])*ticheng[j]
        i=lirun[j]
print("利润为",sum)
