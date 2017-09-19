print("{}网址：'{}!'".format('菜鸟教程','www.runoob.com'))
#两个大括号依次代表format中元素
print('{0} and {1}'.format('a','b'))
print('{1} and {0}'.format('a','b'))
#如果大括号中有数字，则数字代表后面format中元素的位置
#以下是一些其他的用法
print('{name}网址: {site}'.format(name='菜鸟教程',site='www.runoob.com'))
print('{0},{1},{other}'.format('a','b',other='c'))
a=1 
b=2
print('{},{}'.format(a,b))
