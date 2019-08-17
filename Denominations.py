a=list(map(int,input().split()))
a=sorted(a,reverse=True)
s=[0 for i in range(len(a))]
n=int(input())
for i in range(len(a)):
	if n>=a[i]:
		s[i]=n//a[i]
		n=n-s[i]*a[i]
print(sum(s))
