a=list(map(int,input().split()))
s=sum(a)
if s>0:
	print("0")
elif s<0:
	print(abs(s)+1)
else:
	print("1")
