
class Node:
	def __init__(self,data):
		self.left=None
		self.right=None
		self.data=data
	def insert(self,data):
		if self.data:
			if data< self.data:
				if self.left==None:
					self.left=Node(data)
				else:
					self.left.insert(data)
			else:
				if self.right==None:
					self.right=Node(data)
				else:
					self.right.insert(data)
		else:
			self.data=data
"""def preorder(Node):
	if not Node:
		return
	print(Node.data)
	preorder(Node.left)
	preorder(Node.right)"""
			
def leafsum(root):
    global total
    if root is None:
	    return
    if root.left is None and root.right is None:
	    total+=root.data
    leafsum(root.left)
    leafsum(root.right)
n=int(input())
l=list(map(int,input().split()))
root=Node(l[0])
for i in l:
	root.insert(i)
total=0
leafsum(root)
print(total)
#preorder(root)
a=[]
