list=[1,2,3,4]
it=iter(list)
print(next(it))
print(next(it))
for x in it:
   print(x,end=" ")
#该函数输出为
'''
1
2
3 4
'''
#iter返回的是一个迭代器，第一次使用next函数会让迭代器指向第一个元素并且保存位置
