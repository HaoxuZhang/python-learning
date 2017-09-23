letter=input("请输入第一个字母：");
if letter=='M':print("Monday");
elif letter=='W':print("Wednesday");
elif letter=='F':print("Firday");
elif letter=='T':
    letter=input("请输入第二个字母：")
    if letter=='u':print("Tuesday");
    elif letter=='h':print("Thursday");
    else:print("输入错误");
elif letter=='S':
    letter=input("请输入第二个字母：");
    if letter=='a':print("Saturday");
    elif letter=='u':print("Sunday");
    else:print("输入错误");
else:print("输入错误")
