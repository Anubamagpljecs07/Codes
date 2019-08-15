a=input()
a=list(a.split())
c=[]
for i in a:
	c.append(len(i))
m=0
for i in range(0,len(c)):
	if c[i]%2==0 and c[i]>m:
		m=c[i]
		g=i
print(a[g])
	
