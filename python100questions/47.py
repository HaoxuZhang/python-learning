def exchange(a,b):
    a,b=b,a
    return (a,b)
if __name__=='__main__':
    x=10
    y=20
    print(x,y)
    x,y=exchange(x,y)
    print(x,y)
