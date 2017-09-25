'''在函数中，函数被调用结束内存就会释放，无法保存var，var也就不是个静态变量 '''
def varfunc():
    var=0
    print("var=",var)
    var+=1
if __name__=='__main__':
    for i in range(3):
        varfunc()
''' 但是如果定义在类中，可以模仿静态变量储存起来'''
class Static:
    var=0
    def __init__(self,n):
        self.var=n
    def varAdd(self):
        print("var=",self.var)
        self.var+=1
a=Static(5)
for i in range(3):
    a.varAdd()
