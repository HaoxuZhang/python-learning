#该循环用来说明test都干了什么事，每次循环，test代表的是列表中的值，最后发现
#列表中没有test的值，就进入了else。但是每次循环输出的test不是10,是数组中的值
tests=[1,2,3,4,5,6]
test=10
for test in tests:
   print(test)
else: print("没有循环数据")
