'''这个例子让说是模仿静态变量的另一案例，我不明白这道题目想干啥，calss里的是静态变量
定义在全局的也是静态变量，是想描述这个意思？'''
class Num:
    nNum=1
    def inc(self):
        self.nNum+=1
        print('nNum=',self.nNum)

if __name__=='__main__':
    nNum=2
    inst=Num()
    for i in range(3):
        nNum+=1
        print("The num=",nNum)
        inst.inc()
