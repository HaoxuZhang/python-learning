import string
s=input("输入字符串:")
letters=0
space=0
digit=0
others=0
for c in s:
	if c.isalpha():
		letters+=1
	elif c.isspace():
		space+=1
	elif c.isdigit():
		digit+=1
	else:
		others+=1
print(letters,space,digit,others)
