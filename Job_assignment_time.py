a=list(map(int,input().split()))
a=sorted(a)
c,d,e=[],[],[]
j=len(a)-1
if len(a)%2==0:
	for i in range(len(a)):
		if i!=j and i not in e and j not in d:
			c.append(a[i]+a[j])
			d.append(i)
			e.append(j)
			j-=1
	
print(max(c))
