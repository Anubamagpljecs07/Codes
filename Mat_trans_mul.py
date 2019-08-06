r,c=map(int,input().split())
a=[[int(i) for i in input().split()]for j in range(r)]
l=[[a[j][i] for j in range(r)] for i in range(c)]
res=[[0 for i in range(len(l[0]))] for j in range(r)]
for i in range(r):
	for j in range(len(l[0])):
		for k in range(len(l)):
			res[i][j]+=a[i][k]*l[k][j]
print(res)
