a=input()
ch=a[0]
c=0
g=""
for i in range(len(a)):
	if a[i]==ch and i<len(a)-1:
		c+=1
	elif i==len(a)-1 and a[i]==ch:
		c+=1
		g+=ch+str(c)
	
	elif i<len(a)-1 and a[i]!=ch:
		g+=ch+str(c)
		ch=a[i]
		c=1
	else:
		g+=ch+str(c)
		g+=a[-1]+"1"
print(g)
		
