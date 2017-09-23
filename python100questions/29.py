def digitNum(num):
    res=0
    while num!=0:
        num=num//10
        res+=1
    return res
def reverse(s,l):
    if l==0:
        print()
        return
    print(s[l-1],end='')
    reverse(s[:-1],l-1)
s=input("请输入一个正整数：");
num=int(s);
res=digitNum(num);
print("该数为{}位数".format(res));
l=len(s)
reverse(s,l)
