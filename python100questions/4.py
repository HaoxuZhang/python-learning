def isLeapYear(a):
	if (a%4==0 and a%100!=0) or (a%400==0):
		return True
	return False
year=int(input("输入年份:"))
month=int(input("输入月份:"))
day=int(input("输入日期:"))
months=(0,31,59,90,120,151,181,212,243,273,304,334)
result=months[month-1]+day
if isLeapYear(year)==True and month>2:#如果是润年并且月份数大于2,需要加一天
	result+=1
print("It is the {}th day".format(result))
