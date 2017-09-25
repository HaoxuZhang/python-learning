x=[[12,7,3],[4,5,6],[7,8,9]]
y=[[5,8,1],[6,7,3],[4,5,9]]
z=[]
for i in range(3):
    z.append([])
for i in range(3):
    for j in range(3):
        z[i].append(x[i][j]+y[i][j])
for i in z:
    print(i)
