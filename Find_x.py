a=input()
x=a.index('x')
e=a.index("=")
for i in range(1,e):
    if not a[i].isalnum():
        f=i
d=a[0:f]
g=a[f+1:e]
c=0
for i in d:
    if i.isdigit():
        c+=1
if c==len(d):
    num=int(d)
else:
    num=int(g)
if x<e:
    if "+" in a:
        xval=int(a[e+1::])-num
    elif "-" in a:
        xval=int(a[e+1::])+num
    elif "*" in a:
        xval=int(a[e+1::])/num
    else:
    	if not d.isalpha():
    		xval=(1/int(a[e+1::]))*(num)
    	else:
    		xval=int(a[e+1::])*(num)
else:
    if "+" in a:
        xval=int(d)+int(g)
    elif "-" in a:
        xval=int(d)-int(g)
    elif "*" in a:
        xval=int(d)*int(g)
    else:
        xval=int(d)/int(g)
print(xval)
