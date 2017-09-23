def output(s,l):
    if l==0:
        print()
        return
    print(s[l-1],end="")
    output(s[:-1],l-1)
s=input("请输入一段字符串：")
l=len(s)
output(s,l)
