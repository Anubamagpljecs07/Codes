a=input()
c=1
for i in a:
	if a.count(i)>1 and i!=" ":
		c+=1
		g=i
		break
if c==1:
	print("-1")
else:
	print(g)
