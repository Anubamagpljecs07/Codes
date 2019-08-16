a=list(map(int,input().split()))
k=int(input())
c=0
for i in range(0,len(a)):
	for j in range(0,len(a)):
		s=[]
		s=a[i:j+1]
		if sum(s)==k:
			c+=1
print(c)			
