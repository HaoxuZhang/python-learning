n=int(input("请输入学生的成绩："))
if n in range(60):
	grade='C'
elif n in range(60,90):
	grade='B'
else:
	grade='A'
print("该学生成绩的等级为：",grade)
